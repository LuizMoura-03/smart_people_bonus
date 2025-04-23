# smart_people_bonus

Este projeto é um sistema de gerenciamento de recursos humanos (RH) que permite o cadastro de funcionários e o cálculo de seus bônus. A aplicação é desenvolvida em Python e utiliza conceitos de orientação a objetos.

## Finalidade do Projeto

O objetivo deste projeto é fornecer uma ferramenta simples e eficaz para gerenciar informações de funcionários e calcular bônus de forma automatizada, utilizando princípios de programação orientada a objetos.

## Funcionalidades

- **Cadastro de funcionários**: Permite adicionar novos funcionários ao sistema.
- **Cálculo de bônus**: Calcula o bônus de cada funcionário com base em critérios específicos
- **Listagem de bônus**: Exibe uma lista de bônus utilizando polimorfismo para diferentes tipos de funcionários.

## Estrutura do Projeto

- `Funcionario`: Classe base para todos os funcionários.
- `Gerente`: Classe que herda de `Funcionario` e implementa cálculo de bônus específico.
- `SistemaRH`: Classe que gerencia o cadastro e listagem de funcionários.

## Pré-requisitos

- Python 3.x instalado na máquina.

## Passo a Passo para Baixar e Executar o Projeto

1. Clone o repositório para sua máquina local:
   ```bash
   git clone git@github.com:LuizMoura-03/smart_people_bonus.git

2. Navegue até o diretório do projeto.

    Use o comando abaixo para entrar no diretório do projeto:
   ```bash
     cd smart_people_bonus

3. Execute o script principal para iniciar o sistema:
   ```bash
      python main.py

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.      