# Faça um programa que peça o nome de um time de futebol, a quantidade de vitórias e empates.
# Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto, calcule e mostre a pontuação total do time.

# Entrada de dados
time = input("Informe o nome do seu time: ")
vitorias = int(input("Informe o número de vitórias: "))
empates = int(input("Informe o número de empates: "))

# Processamento computacional
pontos = (vitorias * 3) + empates

# Saída de dados

print(f"Time: {time}")
print(f"Total de vitórias: {vitorias}")
print(f"Total de empates: {empates}")
print(f"Total de pontos: {pontos}")