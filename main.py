import numpy as np
import functions as fn

x = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"]
])

while opcion != 5:
    opcion = int(input(
        """
        1. Ver disponibilidad de boletos
        2. Reservar boleto de forma manual
        3. Reserva boleto aleatoriamente
        4. Desocupar asiento
        5. Salir
        """
    ))
    if opcion == 1:
        for i in x:
            print('\t'.join(map(str, i)))
    elif opcion == 2:
        user_column = input ("Ingrese la columna en la cual desea reservar su boleto: ")
        user_row = int(input("Ingrese la fila en la que desea reservar un boleto: "))
        translate = fn.translate_to_number(user_column)
        reservacion = fn.reservar_boleto(x,user_row, translate)
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass



