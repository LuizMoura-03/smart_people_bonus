def logar_acao(func):
    def wrapper(self, funcionario):
        print("Log: Ação de bônus executada")
        return func(self, funcionario)
    return wrapper

class SistemaRH:
    def __init__(self):
        self.funcionarios = []
        
    def cadastrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        
    @logar_acao
    def mostrar_bonus(self, funcionario):
        print(f"Funcionário: {funcionario.get_nome()}, Bônus: {funcionario.calcular_bonus()}")
    
    
    def listar_bonuses(self):
        for funcionario in self.funcionarios:
            self.mostrar_bonus(funcionario)