def reservar_boleto (x, user_row, user_column):
    if x[user_row, user_column] != "X":
        x[user_row, user_column] = "X"
    else:
        print("Asiento ya esta ocupado, intente con otro asiento")
    for i in x:
        print('\t'.join(map(str, i)))

def translate_to_number (n):
    for i in n:
        n = ord(n) - 64
    return n