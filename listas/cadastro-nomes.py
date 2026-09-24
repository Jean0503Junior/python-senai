# Crie uma lista vazia para armazenar nomes.

# Use um for para pedir 3 nomes ao usuário.

# A cada nome digitado, adicione o nome na lista usando append().

# No final, mostre todos os nomes cadastrados.

# Exemplo:

# Digite um nome: João
# Digite um nome: Maria
# Digite um nome: Pedro

# Nomes cadastrados: ['João', 'Maria', 'Pedro']

nomes = []

for i in range(3):

    nome_add = input("Digite um nome: ")

    nomes.append(nome_add)


print("Nomes cadastrados: ", nomes)

for nome_add in nomes:

    print("-", nome_add)