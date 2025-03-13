clientes = []
while True:
    print('\n ==MENU==')
    print('1. Adicionar Cliente')
    print('2. Listar Clientes')
    print('3. Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        nome = input('Digite o nome do cliente: ')
        clientes.append(nome)
    elif opcao == '2':
        print('Clientes cadastrados:')
        for cliente in clientes:
            print(cliente)
    elif opcao == '3':
        break
    else:
        print('Opção inválida, tente novamente.')