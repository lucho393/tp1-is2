import unittest
from rpn import eval_rpn, RPNError


class TestRPN(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(eval_rpn(["3","4","+"]), 7)

    def test_complejo(self):
        self.assertEqual(eval_rpn(["5","1","2","+","4","*","+","3","-"]), 14)

    def test_division_cero(self):
        with self.assertRaises(RPNError):
            eval_rpn(["3","0","/"])

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            eval_rpn(["3","hola","+"])

    def test_pila_final(self):
        with self.assertRaises(RPNError):
            eval_rpn(["3","4"])

    def test_resta(self):
        self.assertEqual(eval_rpn(["5","2","-"]), 3)

    def test_multiplicacion(self):
        self.assertEqual(eval_rpn(["3","4","*"]), 12)

    def test_dup(self):
        self.assertEqual(eval_rpn(["3","dup","+"]), 6)

    def test_swap(self):
        self.assertEqual(eval_rpn(["3","4","swap","-"]), 1)

    def test_sqrt(self):
        self.assertEqual(eval_rpn(["9","sqrt"]), 3)

    def test_log(self):
        self.assertEqual(eval_rpn(["100","log"]), 2)

    def test_sin(self):
        self.assertAlmostEqual(eval_rpn(["90","sin"]), 1, places=2)

    def test_memoria(self):
        self.assertEqual(eval_rpn(["5","STO00","RCL00","+"]), 10)

    def test_ln(self):
        self.assertAlmostEqual(eval_rpn(["1","ln"]), 0, places=2)

    def test_ex(self):
        self.assertAlmostEqual(eval_rpn(["1","ex"]), 2.718, places=2)

    def test_10x(self):
        self.assertEqual(eval_rpn(["2","10x"]), 100)

    def test_inverso(self):
        self.assertEqual(eval_rpn(["2","1/x"]), 0.5)

    def test_chs(self):
        self.assertEqual(eval_rpn(["5","chs"]), -5)

    def test_asin(self):
        self.assertAlmostEqual(eval_rpn(["1","asin"]), 90, places=2)

    def test_acos(self):
        self.assertAlmostEqual(eval_rpn(["1","acos"]), 0, places=2)

    def test_atg(self):
        self.assertAlmostEqual(eval_rpn(["1","atg"]), 45, places=2)

    def test_drop(self):
        self.assertEqual(eval_rpn(["3","4","drop"]), 3)

    def test_clear(self):
        with self.assertRaises(RPNError):
            eval_rpn(["3","4","clear"])


if __name__ == "__main__":
    unittest.main()