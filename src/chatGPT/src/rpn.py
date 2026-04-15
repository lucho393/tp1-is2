import math,sys

class RPNError(Exception):pass

def eval_rpn(t):
 s=[];m={f"{i:02}":0.0 for i in range(10)}
 for x in t:
  try:s.append(float(x));continue
  except:pass
  if x=="p":s.append(math.pi)
  elif x=="e":s.append(math.e)
  elif x=="j":s.append((1+math.sqrt(5))/2)
  elif x in "+-*/":
   if len(s)<2:raise RPNError("Pila insuficiente")
   b,a=s.pop(),s.pop()
   if x=="+":s.append(a+b)
   elif x=="-":s.append(a-b)
   elif x=="*":s.append(a*b)
   elif x=="/":
    if b==0:raise RPNError("División por cero")
    s.append(a/b)
  elif x=="dup":
   if not s:raise RPNError("Pila vacía")
   s.append(s[-1])
  elif x=="swap":
   if len(s)<2:raise RPNError("Pila insuficiente")
   s[-1],s[-2]=s[-2],s[-1]
  elif x=="drop":
   if not s:raise RPNError("Pila vacía")
   s.pop()
  elif x=="clear":s.clear()
  elif x in {"sqrt","log","ln","ex","10x","1/x","chs"}:
   if not s:raise RPNError("Pila vacía")
   a=s.pop()
   if x=="sqrt":
    if a<0:raise RPNError("Raíz negativa")
    s.append(math.sqrt(a))
   elif x=="log":s.append(math.log10(a))
   elif x=="ln":s.append(math.log(a))
   elif x=="ex":s.append(math.exp(a))
   elif x=="10x":s.append(10**a)
   elif x=="1/x":
    if a==0:raise RPNError("División por cero")
    s.append(1/a)
   elif x=="chs":s.append(-a)
  elif x=="yx":
   if len(s)<2:raise RPNError("Pila insuficiente")
   b,a=s.pop(),s.pop();s.append(a**b)
  elif x in {"sin","cos","tg"}:
   if not s:raise RPNError("Pila vacía")
   a=math.radians(s.pop())
   s.append(math.sin(a) if x=="sin" else math.cos(a) if x=="cos" else math.tan(a))
  elif x in {"asin","acos","atg"}:
   if not s:raise RPNError("Pila vacía")
   a=s.pop()
   s.append(math.degrees(math.asin(a)) if x=="asin" else math.degrees(math.acos(a)) if x=="acos" else math.degrees(math.atan(a)))
  elif x.startswith("STO"):
   k=x[3:]
   if k not in m or not s:raise RPNError("Memoria inválida")
   m[k]=s[-1]
  elif x.startswith("RCL"):
   k=x[3:]
   if k not in m:raise RPNError("Memoria inválida")
   s.append(m[k])
  else:raise RPNError(f"Token inválido: {x}")
 if len(s)!=1:raise RPNError("Resultado inválido")
 return s[0]

def main():
 try:
  t=sys.argv[1:] if len(sys.argv)>1 else input().split()
  print(eval_rpn(t))
 except RPNError as e:print("Error:",e)

if __name__=="__main__":main()