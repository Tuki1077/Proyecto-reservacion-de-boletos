import numpy as np
import functions as fn
import linkedprueba as link
import time 

x = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"]
])

menu = True
while menu == True:
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
        y = int(input("Cuantos asientos desea reservar: "))
        contador = 0
        while contador < y:
            user_column = input ("Ingrese la columna en la cual desea reservar su boleto: ")
            user_row = int(input("Ingrese la fila en la que desea reservar un boleto: "))
            silla = str(input("Se requiere servicio especial de silla de ruedas? "))
            translate = fn.translate_to_number(user_column)
            reservacion = fn.reservar_boleto(x,user_row, translate)
            rueda = link.silla(silla, user_row, user_column)
            contador = contador + 1

    elif opcion == 3:
        reservar_random = fn.reservar_random(x)
    elif opcion == 4:
        user_column = input ("Ingrese la columna que desea remover: ")
        user_row = int(input("Ingrese la fila que desea remover: "))
        silla = str(input("Necesitaba de servicios especiales? "))
        translate = fn.translate_to_number(user_column)
        if silla == "si":
            ruedo = "si"
            remover = fn.remover_boleto(x, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
        else:
            ruedo = "no"
            remover = fn.remover_boleto(x, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
    elif opcion == 5:
        print ("Gracias por utilizar nuestros servicios!...")
        menu = False