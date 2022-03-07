import numpy as np
import functions as fn
import linkedprueba as link
import time 

A138 = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"],
    ["4","0","0","0","0","0","0"],
    ["5","0","0","0","0","0","0"],
    ["6","0","0","0","0","0","0"],
    ["7","0","0","0","0","0","0"],
    ["8","0","0","0","0","0","0"],
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
        for i in A138:
            print('\t'.join(map(str, i)))
    elif opcion == 2:
        y = int(input("Cuantos asientos desea reservar: "))
        contador = 0
        while contador < y:
            user_column = input ("Ingrese la columna en la cual desea reservar su boleto: ")
            user_row = int(input("Ingrese la fila en la que desea reservar un boleto: "))
            silla = str(input("Se requiere servicio especial de silla de ruedas? (Y/N) "))
            print ("\n Procesando su solicitud... ")
            time.sleep(2)
            translate = fn.translate_to_number(user_column)
            reservacion = fn.reservar_boleto(A138,user_row, translate)
            rueda = link.silla(silla, user_row, user_column)
            contador = contador + 1

    elif opcion == 3:
        reservar_random = fn.reservar_random(A138)
    elif opcion == 4:
        user_column = input ("Ingrese la columna que desea remover: ")
        user_row = int(input("Ingrese la fila que desea remover: "))
        silla = str(input("Necesitaba de servicios especiales? "))
        translate = fn.translate_to_number(user_column)
        if silla == "Y":
            ruedo = "Y"
            remover = fn.remover_boleto(A138, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
        else:
            ruedo = "N"
            remover = fn.remover_boleto(a138, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
    elif opcion == 5:
        print ("Gracias por utilizar nuestros servicios!...")
        menu = False