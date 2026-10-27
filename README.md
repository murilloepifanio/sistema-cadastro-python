# Sistema de Cadastro de Pessoas em Python

Projeto desenvolvido em **Python** com o objetivo de praticar conceitos fundamentais da linguagem por meio da criação de um sistema simples de cadastro de pessoas.

O sistema permite cadastrar pessoas, listar todos os registros armazenados e consultar uma pessoa pelo nome.

## Funcionalidades

O programa possui as seguintes funcionalidades:

* Cadastrar uma pessoa
* Listar todas as pessoas cadastradas
* Consultar uma pessoa pelo nome
* Validar idade e salário
* Tratar entradas inválidas no menu
* Encerrar o programa através de um menu interativo

## Dados armazenados

Cada pessoa cadastrada possui:

* Nome
* Idade
* Salário

Os dados são armazenados em uma lista de dicionários.

Exemplo da estrutura utilizada:

```python
cadastro = [
    {
        "nome": "Carlos",
        "idade": 30,
        "salario": 3500.00
    }
]
```

## Conceitos de Python utilizados

Durante o desenvolvimento deste projeto foram utilizados:

* Funções
* Parâmetros
* `**kwargs`
* Listas
* Dicionários
* Estruturas condicionais (`if`, `elif`, `else`)
* Laço `while`
* Laço `for`
* `try` e `except`
* `raise`
* `ValueError`
* `return`
* `len()`
* Método `.append()`
* Método `.lower()`
* F-strings
* Formatação de valores monetários
* `if __name__ == "__main__"`

## Estrutura do programa

O projeto foi dividido em funções para separar as responsabilidades do sistema:

```text
cadastrar()
    ↓
Adiciona os dados na lista de cadastros

informar_dados()
    ↓
Recebe e valida os dados da pessoa

listar_informacoes()
    ↓
Exibe todas as pessoas cadastradas

consulta_pessoa()
    ↓
Pesquisa uma pessoa pelo nome

menu_principal()
    ↓
Controla a execução do programa
```

## Menu

Ao executar o programa, o usuário encontra o seguinte menu:

```text
===== SISTEMA DE CADASTRO =====

1 - Cadastrar pessoa
2 - Listar pessoas
3 - Consultar pessoa
0 - Sair
```

## Validações

O programa possui algumas validações para evitar dados inválidos.

A idade deve estar entre **0 e 110 anos**.

O salário não pode ser negativo.

Também existe tratamento para impedir que valores não numéricos sejam utilizados nas opções do menu.

## Como executar

Tenha o Python instalado no computador.

Clone o repositório:

```bash
git clone https://github.com/murilloepifanio/sistema-cadastro-python.git
```

Entre na pasta do projeto:

```bash
cd sistema-cadastro-python
```

Execute:

```bash
python main.py
```

## Objetivo do projeto

Este projeto faz parte dos meus estudos de **Python**, tendo como objetivo aplicar na prática os fundamentos da linguagem antes de avançar para projetos envolvendo arquivos, orientação a objetos, bancos de dados e análise de dados.

## Próximas melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* Editar uma pessoa cadastrada
* Excluir um cadastro
* Criar um ID único para cada pessoa
* Validar o nome informado
* Evitar cadastros duplicados
* Salvar os dados em arquivo JSON
* Carregar os dados automaticamente ao iniciar o programa
* Migrar o armazenamento para SQLite
* Adicionar orientação a objetos
* Criar testes automatizados
* Criar uma interface gráfica ou web

## Autor

**Murillo Epifânio Rodrigues de Almeida**

Projeto desenvolvido para fins de estudo e prática de programação em Python.
