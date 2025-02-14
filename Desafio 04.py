'''
Faça uma função que calcula a media das notas de uma lista de dicionarios de estudantes.
A função deve receber um dicionario onde as chaves são os nomes dos estudantes e os valores são listas com as notas deles. 
Essa função deve retornar os dicionarios como uma informação se o aluno passou ou não.
'''
Alunos = {
    "João Vitor": [7.5, 8.0, 6.8, 9.2, 7.0],
    "Mariana": [8.9, 9.5, 7.8, 5.0, 4.8],
    "Thiago": [2.5, 3.2, 4.5, 6.9, 5.0],
    "Camila": [9.0, 8.7, 4.0, 3.5, 6.8],
    "Gustavo": [7.8, 5.5, 6.0, 3.8, 4.2]
}

def Calcular (nome):
    i = 0
    media = 0
    while i < 5:
        media += Alunos[nome][i]
        i+=1
    print("A media das notas de",nome, "é", round((media/5), 2))
    if (media/5) >= 7:
        print("Está aprovado ★")
    else:
        print("Melhor sorte no proximo ano ☹")

nome = input("Digite o nome do aluno que você gostaria de verificar a media: ")

Calcular(nome)
