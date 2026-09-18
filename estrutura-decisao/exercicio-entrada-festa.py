# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print(f"{nome} você pode entrar na festa!")
elif idade > 15 and idade < 18:
    print(f"{nome} você pode entrar com responsável!")
else:
    print(f"{nome} você não pode entrar na festa!")