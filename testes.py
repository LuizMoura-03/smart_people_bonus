import unittest
from funcionarios import FuncionarioComum, Gerente

class TestFuncionarios(unittest.TestCase):
    def test_calculo_bonus_funcionario_comum(self):
        funcionario = FuncionarioComum("João", 2000)
        self.assertEqual(funcionario.calcular_bonus(), 200)
        
    def test_calculo_bonus_gerente(self):
        gerente = Gerente("Luiz", 4000, 1000)
        self.assertEqual(gerente.calcular_bonus(), 1800)

    def test_set_salario_negativo(self):
        funcionario = FuncionarioComum("João", 2000)
        with self.assertRaises(ValueError):
            funcionario.set_salario(-200)
            
    def test_set_salario_negativo_gerente(self):
        gerente = Gerente("Luiz", 4000, 1000)
        with self.assertRaises(ValueError):
            gerente.set_salario(-4000)

if __name__ == '__main__':
    unittest.main()