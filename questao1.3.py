# Parte A: Mensagem de boas-vindas
print("+-----------------------------------+")
print("| Bem-vindo ao sistema de cobrança  |")
print("|     do Petshop Daniel M. Yomoto!  |")
print("+-----------------------------------+\n")

# Função para obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro (em kg): "))
            if peso < 3:
                return 40
            elif 3 <= peso < 10:
                return 50
            elif 10 <= peso < 30:
                return 60
            elif 30 <= peso < 50:
                return 70
            else:
                print("Peso inválido. O peso deve ser menor que 50 kg.")
        except ValueError:
            print("Valor inválido. Digite um número.")

# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        print("+-----------------------------------+")
        print("| Escolha o tipo de pelo do cachorro|")
        print("+-----------------------------------+")
        print("| c) Curto                          |")
        print("| m) Médio                          |")
        print("| l) Longo                          |")
        print("+-----------------------------------+")
        pelo = input("Opção: ").lower()
        if pelo in ['c', 'm', 'l']:
            if pelo == 'c':
                return 1
            elif pelo == 'm':
                return 1.5
            elif pelo == 'l':
                return 2
        else:
            print("Opção de pelo inválida. Digite c para curto, m para médio ou l para longo.")

# Função para obter os serviços adicionais
def cachorro_extra():
    extras = {'1': 'Cortar unhas (R$10)', '2': 'Escovar dentes (R$12)', '3': 'Limpar orelhas (R$15)', '0': 'Não querer mais nada'}
    total_extra = 0
    escolhas_feitas = []

    while True:
        print("+---------------------------------------+")
        print("| Escolha um serviço adicional          |")
        print("+---------------------------------------+")
        for chave, valor in extras.items():
            if chave not in escolhas_feitas:
                print(f"| {chave}) {valor.ljust(34)} |")
        print("+---------------------------------------+")

        adicional = input("Opção: ")
        if adicional == '0':
            break
        elif adicional in extras and adicional not in escolhas_feitas:
            total_extra += extras_valor[adicional]
            escolhas_feitas.append(adicional)
        else:
            print("Opção inválida ou já escolhida. Escolha novamente.")

    return total_extra

try:
    # Parte E: Calcular o total a pagar
    peso_base = cachorro_peso()
    pelo_mult = cachorro_pelo()
    extras_valor = {'1': 10, '2': 12, '3': 15}
    extra_valor = cachorro_extra()

    total = peso_base * pelo_mult + extra_valor

    # Parte F: Saída de resultados
    print("\nResultado:")
    
    print(f"Total a pagar: R${total:.2f}")

except ValueError:
    print("\nErro: Valor não numérico para o peso.")

except:
    print("\nErro desconhecido.")
