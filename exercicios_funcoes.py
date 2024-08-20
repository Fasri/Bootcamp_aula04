# 16.Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# def somar_lista(lista_numeros):
#     soma = 0
#     for numero in lista_numeros:
#         soma = numero + soma
#     return soma

# lista = [2,4,5,8]

# print(somar_lista(lista))

# 17.Crie uma função que receba um número como argumento e retorne True se o número for primo 
# e False caso contrário.

# def eh_primo(numero:int):
#     if numero <= 1:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True
    

# print(eh_primo(17))

# 18.Desenvolva uma função que receba uma string como argumento e 
# retorne essa string revertida.

# def reverte_string(original:str):
#     return original[::-1]

# print(reverte_string("teste"))
# print(reverte_string("Gilcilena"))

# 19.Implemente uma função que receba dois argumentos: uma lista de números e um número.
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def fazer_pares(lista:list, numero:int):
    soma =[]
    for i in lista:
        soma.append(i+numero)
    return soma
lista1=[4,5,6,7,10]
numero1 = 9
print(fazer_pares(lista1, numero1))


# 20.Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas