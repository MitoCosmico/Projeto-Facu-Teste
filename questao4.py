# Parte A: Mensagem de boas-vindas
print("Bem-vindo ao Controle de Colaboradores de Daniel Mitsonosuke Yomoto!")

# Criação da lista vazia de colaboradores e variável global de id
lista_colaboradores = []
id_global = 1

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    global id_global
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    pagamento = float(input("Digite o pagamento do colaborador: "))
    
    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "pagamento": pagamento
    }
    
    lista_colaboradores.append(colaborador)
    id_global += 1
    print("Colaborador cadastrado com sucesso!\n")

# Função para consultar colaboradores
def consultar_colaborador():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nLista de todos os colaboradores:")
            for colaborador in lista_colaboradores:
                print(f"ID: {colaborador['id']} | Nome: {colaborador['nome']} | Setor: {colaborador['setor']} | Pagamento: R${colaborador['pagamento']:.2f}")
        elif opcao == '2':
            id_busca = int(input("Digite o ID do colaborador: "))
            colaborador_encontrado = None
            for colaborador in lista_colaboradores:
                if colaborador['id'] == id_busca:
                    colaborador_encontrado = colaborador
                    break
            if colaborador_encontrado:
                print("Colaborador encontrado:")
                print(f"Nome: {colaborador_encontrado['nome']} | Setor: {colaborador_encontrado['setor']} | Pagamento: R${colaborador_encontrado['pagamento']:.2f}")
            else:
                print("Colaborador não encontrado.")
        elif opcao == '3':
            setor_busca = input("Digite o setor: ")
            print(f"\nLista de colaboradores no setor {setor_busca}:")
            for colaborador in lista_colaboradores:
                if colaborador['setor'] == setor_busca:
                    print(f"ID: {colaborador['id']} | Nome: {colaborador['nome']} | Pagamento: R${colaborador['pagamento']:.2f}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Escolha novamente.\n")

# Função para remover um colaborador
def remover_colaborador():
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    colaborador_encontrado = None
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_remover:
            colaborador_encontrado = colaborador
            break
    if colaborador_encontrado:
        lista_colaboradores.remove(colaborador_encontrado)
        print("Colaborador removido com sucesso!\n")
    else:
        print("Colaborador não encontrado.\n")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")
    opcao_menu = input("Escolha uma opção: ")
    
    if opcao_menu == '1':
        cadastrar_colaborador(id_global)
    elif opcao_menu == '2':
        consultar_colaborador()
    elif opcao_menu == '3':
        remover_colaborador()
    elif opcao_menu == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Escolha novamente.\n")
