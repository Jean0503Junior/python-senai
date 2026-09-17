# Entrada de dados básicos
nome = input("Informe seu nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

# Processamento computacional
media = (n1 + n2) / 2

# Saída das informações
# Formatação com uma casa decimal
# f -> significa número de ponto flutuante (decimal)
# .1 - > significa mostrar uma casa decimal
print(f"{nome} sua média é: {media: .1f}")    