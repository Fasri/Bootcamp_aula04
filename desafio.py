CONSTANTE_BONUS:float = 1000




# 1) Solicite ao usuário que digite seu nome

def nome_usuário (nome):
    nome_valido:bool = False
    while not nome_valido:
        try:
            nome_usuario:str = nome
            if len(nome_usuario) ==0:
                raise ValueError("O nome está vazio.")
                
            elif any(char.isdigit() for char in nome_usuario):
                raise ValueError("O nome não deve conter números.")
                
            elif nome_usuario.isspace():
                print("Você só digitou espaço!")
                
            else:
                nome_valido = True
        except ValueError as e:
            print(e)
    return nome_usuario
        

# 2) Solicite ao usuário que digite o valor do seu salário
# Converta a entrada para um número de ponto flutuante

def salario_valido(salario_usuario):
    salario_valido:bool = False
    while not salario_valido:
        try:
            salario_usuario:float = salario_usuario
            if salario_usuario< 0:
                print("O sálario tem que ser um valor positivo!")
            else:
                salario_valido = True

        except ValueError:
            print("Digite um número para o sálario!")
    return salario_usuario    

# 3) Solicite ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante
def bonus_eh_valido(bonus_usuario):
    bonus_valido:bool = False
    while not bonus_valido:
        try:
            bonus_usuario:float = bonus_usuario
            if bonus_usuario < 0:
                print("Digite um valor positivo!")
            else:
                bonus_valido = True    
        except ValueError:
            print("Digite um número para o bônus!")
    return bonus_usuario    

# 4) Calcule o valor do bônus final
def calcular_bonus_final(salario_usuario:float,bonus_usuario:float):
    valor_do_bonus:float = CONSTANTE_BONUS + salario_usuario*bonus_usuario
    return valor_do_bonus

# 5) Imprima a mensagem persolazida incluindo o nome do usuário,e o valor do bônus
def mensagem_do_valor_bonus(nome_usuario,salario_usuario,bonus):
    nome_usuario = nome_usuário(nome_usuario)
    salario = salario_valido(salario_usuario)
    bonus = bonus_eh_valido(bonus)
    valor_do_bonus = calcular_bonus_final(salario,bonus)
    print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")

mensagem_do_valor_bonus("Felipe", 1000, 200)