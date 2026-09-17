# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados
produto = input("Insira o nome do produto: ")
preco_produto = float(input("Insira o valor do poduto (R$): "))
quantidade_produto = int(input("Insira a quantidade de produtos a ser comprada: "))

# Processamento computacional
total_compra = preco_produto * quantidade_produto

# Saída de dados
print(f"Produto: {produto}")
print(f"Preço do produto: R${preco_produto: .2f}")
print(f"Quantidade comprada: {quantidade_produto}")
print(f"Valor total da compra: R${total_compra: .2f}")