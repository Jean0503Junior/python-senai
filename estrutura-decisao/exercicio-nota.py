# Faça um programa em Python que peça a nota de um aluno e verifique se ele foi aprovado ou reprovado.

# Nota maior ou igual a 6 → Aprovado
# Nota menor que 6 → Reprovado

nota = float(input("Insira sua nota: "))

if nota >= 6:
    print("Você está aprpvado!")
else:
    print("Você reprovou!")