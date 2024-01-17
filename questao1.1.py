# Parte A: Boas-Vindas
print("Bem-vindo a Loja do Daniel Mitsonosuke Yomoto!")

# Parte B: Entrada de valor unitário e quantidade
valor_unitario = float(input("Valor do produto: "))
quantidade = int(input("Quantidade do produto: "))

# Parte C: Cálculo do valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Utilização de estruturas if, elif e else (Parte D)
if quantidade < 200:
    desconto = 0
elif quantidade < 1000:
    desconto = 0.05
elif quantidade < 2000:
    desconto = 0.1
else:
    desconto = 0.15

# Cálculo do valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)

# Parte F: Saída com pedido e desconto
print("\nPedido:")
print(f"Quantidade: {quantidade}")
print(f"Valor unitário: R${valor_unitario:.2f}")
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")
