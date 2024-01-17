# Parte A: Mensagem de boas-vindas
titulo = "Bem-vindo a Sorveteria Daniel M. Yomoto!"
print(titulo)
# Tabela de preços
tabela_precos = {
    ('tr', 1): 6, ('pr', 1): 7, ('es', 1): 8,
    ('tr', 2): 11, ('pr', 2): 13, ('es', 2): 15,
    ('tr', 3): 15, ('pr', 3): 18, ('es', 3): 21
}
print("Tabela de Preços:")
print("+--------------+---------------+--------------+--------------+")
print("| Sabor        | 1 bola (R$)   | 2 bolas (R$) | 3 bolas (R$) |")
print("+--------------+---------------+--------------+--------------+")
print("| Tradicional  | 6             | 11           | 15           |")
print("| Premium      | 7             | 13           | 18           |")
print("| Especial     | 8             | 15           | 21           |")
print("+--------------+---------------+--------------+--------------+\n")
total_final = 0  # Variável para armazenar o total acumulado de pedidos
# Lista para armazenar os pedidos para a tabela
tabela_pedidos = []
# Loop principal
while True:
    # Parte B: Entrada de sabor e quantidade
    while True:
        sabor = input("\nEscolha o sabor do sorvete (tr para Tradicional, pr para Premium, es para Especial): ").lower()
        if sabor in ['tr', 'pr', 'es']:
            break
        else:
            print("Sabor de Sorvete Inválido")
    while True:
        try:
            quantidade = int(input("Digite a quantidade de bolas de sorvete (1, 2 ou 3): "))
            if quantidade in [1, 2, 3]:
                break
            else:
                print("Quantidade de Bolas de Sorvete Inválida")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro (1, 2 ou 3).")

    valor_total = tabela_precos[(sabor, quantidade)]  # Busca o preço na tabela

    total_final += valor_total  # Acumulando o total dos pedidos
    # Adicionando o pedido à tabela
    tabela_pedidos.append((sabor, quantidade, valor_total))
    # Parte E: Pergunta sobre mais pedidos
    while True:
        mais_pedidos = input("\nDeseja pedir mais alguma coisa? (s para Sim, n para Não): ").lower()
        if mais_pedidos in ['s', 'n']:
            break
        else:
            print("Resposta inválida. Digite 'S' para Sim ou 'N' para Não.")
    if mais_pedidos == 'n':
        break  # Encerrar o loop
# Parte F: Saída com tabela de resultados
print("\n" + "-" * 49)
print("| Sabor\t\t| Quantidade\t| Valor Total\t|")
print("-" * 49)
for pedido in tabela_pedidos:
    sabor, quantidade, valor_total = pedido
    print(f"| {sabor}\t\t| {quantidade}\t\t| R${valor_total:.2f}\t|")
print("-" * 49)
print(f"\nValor total do pedido: R${total_final:.2f}")