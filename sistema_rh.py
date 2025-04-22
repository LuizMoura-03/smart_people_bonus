def logar_acao(func):
    def wrapper(funcionario):
        print("Log: Ação de bônus executada")
        return func(funcionario)
    return wrapper