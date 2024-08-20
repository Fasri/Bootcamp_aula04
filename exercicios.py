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
# livro1 ={
#     "Titulo":"Psicologia Financeira",
#     "Autor":"Caleb",
#     "Ano de publicação": 2009
# }

# print(livro1)
# for chave, valor in livro1.items():
#     print(f"{chave}:{valor}")
# 4.Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# 5.Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# frutas = ["maçã", "banana", "cereja"]
# dici_frutas = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(dici_frutas[item] for item in frutas)
# print(f"Preço total: {total}")

#Eliminação de Duplicatas
#6. Dada uma lista de emails, remover todos os duplicados.
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails)) #list cria a lista, set tira os valores duplicados

# print(emails_unicos)

#Filtragem de Dados
#7.Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [4.6,90,45,34,56,3,25]
# maiores=[]
# for idade in idades:
#     if idade>18:
#         maiores.append(idade)
#     else:
#         maiores
# print(maiores)

# Ordenação Personalizada
# 8.Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)e

# Agregação de Dados
# 9.Dado um conjunto de números, calcular a média.
# numeros = [2,9,8,3,5,8,4,7]
# media = sum(numeros)/len(numeros)
# print(media)

# Divisão de Dados em Grupos
# 10. Dada uma lista de valores, dividir em duas listas: 
# uma para valores pares e outra para ímpares.

# numeros = [1,2,3,4,5,6,7,8,9,10]
# pares=[]
# impares = []
# for numero in numeros:
#     if numero%2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
# print(pares)
# print(impares)

# Atualização de Dados
# 11. Dada uma lista de dicionários representando produtos, 
# atualizar o preço de um produto específico.
# produtos = [{"Produto": "Geladeira","Preço":23},
#             {"Produto": "Cafeteira","Preço":15}, 
#             {"Produto": "Televisão","Preço":45}]

# for produto in produtos:
#     if produto["Produto"]=="Cafeteira":
#         produto["Preço"] = 69
# print(produtos)

# Fusão de Dicionários
# 12. Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {
#     "Produt1":"Ferro",
#     "Preço1":23
# }
# dicionario2 = {
#     "Produto":"Regador",
#     "Preço":5
# }

# dicionario1.update(dicionario2)
# print (dicionario1)

# Filtragem de Dados em Dicionário
# 13.Dado um dicionário de estoque de produtos, 
# filtrar aqueles com quantidade maior que 0.

# estoque = {"Cadeira":3, "Televisão":0, "Celular": 4, "Monitor": 0}
# positivo= {produto: quantidade for produto,quantidade in estoque.items() if quantidade > 0}
# print(positivo)

# Extração de Chaves e Valores
# 14. Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {
    "casa": "azul",
    "quartos": 3,
    "banheiros": 2
}

chaves =[list(dicionario.keys())]
valores = [list(dicionario.values())]

print("Chaves:", chaves)
print("Valores:", valores)