
 cadastro = []

# cadastro de informações
def cadastrar(**dados):
    cadastro.append(dados)


def informar_dados():
    nome = input('Informe o nome: ')

    idade = int(input('Informe a idade: '))

    if idade > 110 or idade < 0:
        raise ValueError('Informe uma idade válida')

    salario = float(input('Informe o salário: '))

    if salario < 0:
        raise ValueError('Informe o salário corretamente')

    cadastrar(
        nome=nome,
        idade=idade,
        salario=salario
    )


# listagem de informações
def listar_informacoes():

    if len(cadastro) == 0:
        print('Não existem cadastros no banco.')
        return

    for item in cadastro:

        print(f'''
        Nome: {item['nome']}
        Idade: {item['idade']}
        Salário: R$ {item['salario']:.2f}
        ''')

    print('COLABORADORES LISTADOS.')


# consulta pessoa
def consulta_pessoa():

    if len(cadastro) == 0:
        print('Não existem pessoas cadastradas.')
        return

    consulta_nome = input('Informe o nome da pessoa: ')

    encontrado = False

    for item in cadastro:

        if item['nome'].lower() == consulta_nome.lower():

            print('Nome encontrado\n')

            print(f'''
            Nome: {item['nome']}
            Idade: {item['idade']}
            Salário: R$ {item['salario']:.2f}
            ''')

            encontrado = True

    if encontrado == False:
        print('Pessoa não encontrada.')


# menu principal
def menu_principal():

    escolha = -1

    try:

        while escolha != 0:

            print('''
            ===== SISTEMA DE CADASTRO =====

            1 - Cadastrar pessoa
            2 - Listar pessoas
            3 - Consultar pessoa
            0 - Sair
            ''')

            try:

                escolha = int(input('Informe uma opção: '))

                if escolha > 3 or escolha < 0:
                    print('Informe uma das opções acima.')
                    continue

                if escolha == 1:

                    try:
                        informar_dados()

                    except ValueError as erro:
                        print(erro)

                elif escolha == 2:
                    listar_informacoes()

                elif escolha == 3:
                    consulta_pessoa()

            except ValueError:
                print('A opção precisa ser um número inteiro.')

    finally:
        print('''
        Programa finalizado
        ''')


if __name__ == "__main__":
    menu_principal()
