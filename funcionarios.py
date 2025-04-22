from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self._nome

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("Salário não pode ser negativo")
        self._salario = salario