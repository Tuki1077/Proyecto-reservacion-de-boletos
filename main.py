import numpy as np
import functions as fn

x = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","X","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"]
])

for i in x:
    print('\t'.join(map(str, i)))

user_column = input ("Ingrese la columna en la cual desea reservar su boleto: ")
user_row = int(input("Ingrese la fila en la que desea reservar un boleto: "))



translate = fn.translate_to_number(user_column)
print(translate)
reservacion = fn.reservar_boleto(x,user_row, translate)
print(reservacion)



