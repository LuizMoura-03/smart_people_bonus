from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def main():
    funcionario1 = FuncionarioComum("Joã0", 2000)
    gerente1 = Gerente("Luiz", 4000, 1000)

    sistema_rh = SistemaRH()
    sistema_rh.cadastrar_funcionario(funcionario1)
    sistema_rh.cadastrar_funcionario(gerente1)

    sistema_rh.listar_bonuses()

if __name__ == "__main__":
    main()