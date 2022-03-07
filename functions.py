import random as ran
import linkedprueba as link

#busca dentro del array para ver si esta o no disponible el asiento para marcarlo con X
def reservar_boleto (x, user_row, user_column):
    if x[user_row, user_column] != "X":
        x[user_row, user_column] = "X"
        return True
    else:
        return False

#imprime el array
def imprimir_asientos (x):
    for i in x:
        print('\t'.join(map(str, i)))

#esta funcion agara la letra de la fila y la convierte en un numero para recorrer el array
def translate_to_number (n):
    for i in n:
        n = ord(n) - 64
    return n

#funcion de reserva de asiento random, la funcion agarra una fila random y una columna random asi reservando lo que salga
def reservar_random(x):
    columna = ["A", "B", "C", "D", "E", "F"]
    fila = [1,2,3,4,5,6,7,8]
    rueda = "N"
    random_num = ran.choice(columna)
    random_row = ran.choice(fila)
    random_column = translate_to_number(random_num)
    if x[random_row, random_column] != "X":
        x[random_row, random_column] = "X"
    else:
        print("Asiento ya esta ocupado, intente con otro asiento")
    prio = link.silla(rueda, random_row, random_num)
    
    #remoueve la X de la reserva reemplazandole con 0 otra vez
def remover_boleto (x, user_row, user_column):
    if x[user_row, user_column] != "0":
        x[user_row, user_column] = "0"
        return True
    else:
        return False

    #Used for testing 
def random_for_testing (x):
    columna = ["A", "B", "C", "D", "E", "F"]
    fila = [1,2,3,4,5,6,7,8]
    random_num = ran.choice(columna)
    random_row = ran.choice(fila)
    random_column = translate_to_number(random_num)
    if x[random_row, random_column] != "X":
        x[random_row, random_column] = "X"
        return True
    else:
        return False

