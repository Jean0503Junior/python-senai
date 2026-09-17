# Faça um programa que peça o ano de nascimento de uma pessoa e calcule a sua idade atual.
# Depois, mostre o ano de nascimento e a idade no terminal.

# Entrada de dados
ano_nascimento = int(input("Informe seu ano de nascimento: "))

# Processamento de dados
idade = 2026 - ano_nascimento

# Saída de dados
print(f"você nasceu no ano de {ano_nascimento}")
print(f"Você tem {idade} anos")