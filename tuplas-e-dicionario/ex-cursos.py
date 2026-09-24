# Enunciado:
# Crie uma tupla com 5 cursos. Use for e if para verificar se o curso "Python" está presente.

# Tupla com cursos
cursos = ("Python", "Java", "HTML", "JavaScript", "C++")

for curso in cursos:
    if curso == "Python":
        print("O curso python está presente: ", curso)
    else:
        print("O curso de python não está presente: ", curso)