# Entrada de dados
preco = float(input("Digite o preço do produto (R$): "))
desconto = float(input("Digite o valor do desconto (%): "))

# Processamento computacional
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Saída de dados
print(f"Valor do produto: R${preco: .2f}")
print(f"Desconto aplicado: %{desconto: .1f}")
print(f"Valor final do desconto: R${valor_desconto: .2f}")
print(f"O valor final do produto será: R${preco_final: .2f}")