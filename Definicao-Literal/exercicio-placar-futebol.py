# Objetivo:
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de golos marcados por cada equipa.

# Depois, apresente o placar e calcule o total de golos da partida.

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO       
# ================================
# França 3 x 2 Espanha
# Total de golos: 5
# ================================

t1 = "França"
t2 = "Espanha"

golsT1 = 3
golsT2 = 4

totalGols = golsT1 + golsT2

print("================================")
print(        "RESULTADO DO JOGO"       )
print("================================")
print(f"{t1} {golsT1} x {golsT2} {t2}")
print("Total de gols:", totalGols)