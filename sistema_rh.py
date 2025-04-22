def logar_acao(func):
    def wrapper(funcionario):
        print("Log: Ação de bônus executada")
        return func(funcionario)
    return wrapper

class SistemaRH:
    @logar_acao
    def mostrar_bonus(self, funcionario):
        print(f"Funcionário: {funcionario.get_nome()}, Bônus: {funcionario.calcular_bonus()}")