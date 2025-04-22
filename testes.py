import unittest
from funcionarios import FuncionarioComum

class TestFuncionarios(unittest.TestCase):
    def test_calculo_bonus_funcionario_comum(self):
        funcionario = FuncionarioComum("João", 2000)
        self.assertEqual(funcionario.calcular_bonus(), 200)

    def test_set_salario_negativo(self):
        funcionario = FuncionarioComum("João", 2000)
        with self.assertRaises(ValueError):
            funcionario.set_salario(-200)

if __name__ == '__main__':
    unittest.main()