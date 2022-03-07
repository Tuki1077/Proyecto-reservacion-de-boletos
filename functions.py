import random as ran

def reservar_boleto (x, user_row, user_column):
    if x[user_row, user_column] != "X":
        x[user_row, user_column] = "X"
    else:
        return("Asiento ya esta ocupado, intente con otro asiento")
    for i in x:
        print('\t'.join(map(str, i)))

def translate_to_number (n):
    for i in n:
        n = ord(n) - 64
    return n

def reservar_random(x):
    columna = ["A", "B", "C", "D", "E", "F"]
    fila = [1,2,3]
    random_num = ran.choice(columna)
    random_row = ran.choice(fila)
    random_column = translate_to_number(random_num)
    if x[random_row, random_column] != "X":
        x[random_row, random_column] = "X"
    else:
        print("Asiento ya esta ocupado, intente con otro asiento")
    for i in x:
        print('\t'.join(map(str, i)))
    
def remover_boleto (x, user_row, user_column):
    if x[user_row, user_column] != "0":
        x[user_row, user_column] = "0"
    else:
        return("Asiento no esta ocupado, intente con otro asiento")
    for i in x:
        print('\t'.join(map(str, i)))

