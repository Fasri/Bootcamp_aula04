# 1.Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = [1,2,3,4,5,5,7,8,9,10]
# for numero in numeros:
#     quadrado = numero**2
#     print(quadrado)

# 2.Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagem = ["Python", "Java", "C++", "JavaScript"]
# linguagem.remove("C++")
# print(linguagem)
# linguagem.append("Ruby")
# print(linguagem)



# 3.Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro1 ={
    "Titulo":"Psicologia Financeira",
    "Autor":"Caleb",
    "Ano de publicação": 2009
}

print(livro1)
for chave, valor in livro1.items():
    print(f"{chave}:{valor}")
# 4.Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5.Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
