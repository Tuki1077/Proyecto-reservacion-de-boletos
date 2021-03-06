import numpy as np
import functions as fn
import linkedprueba as link
import stack as stack
import time 
import grafo as graf

print ("""
                                                        __  _
                                                        \ `/ |    Bienvenidos a Reserva tu boleto           
                                                        \__`!
                                                        / ,' `-.__________________
                                                        '-'\___  Churro airlines   `-.
                                                        <____()-=O=O=O=O=O=[]====--)
                                                            `.___ ,-----,_______...-'
                                                                /    .'
                                                                /   .'
                                                                /  .'         
                                                                `-'
""")
#creacion del array
Arr = np.array( [
    ["","A","B","C","D","E","F"],
    ["1","0","0","0","0","0","0"],
    ["2","0","0","0","0","0","0"],
    ["3","0","0","0","0","0","0"],
    ["4","0","0","0","0","0","0"],
    ["5","0","0","0","0","0","0"],
    ["6","0","0","0","0","0","0"],
    ["7","0","0","0","0","0","0"],
    ["8","0","0","0","0","0","0"]
])
#menu principal
menu = True
while menu == True:
    print ("""
                            1. Ver disponibilidad de boletos                 6. Despegar avion
                            2. Ver asientos ya reservados                    7. Agregar avion de hangar a lista de espera
                            3. Reservar boleto de forma manual               8. Ver Rutas del Dia
                            4. Reserva boleto aleatoriamente                 9. Ver rutas de aerolinea 
                            5. Desocupar asiento                             10. Salir
    """)
    opcion = int(input())
    #imprimir array
    if opcion == 1:
        for i in Arr:
            print('\t'.join(map(str, i)))
        print (link.llist)

    elif opcion == 2:
        asiento_reservado = list(zip(*np.where(Arr == "X")))
        print (asiento_reservado)
        #reserva de asientos ya sea silla de ruedas o normal
    elif opcion == 3:
        y = int(input("Cuantos asientos desea reservar: "))
        contador = 0
        while contador < y:
            user_column = input ("Ingrese la columna en la cual desea reservar su boleto: ")
            user_row = int(input("Ingrese la fila en la que desea reservar un boleto: "))
            silla = str(input("Se requiere servicio especial de silla de ruedas? (Y/N) "))
            print ("\n Procesando su solicitud... ")
            time.sleep(2)
            translate = fn.translate_to_number(user_column)
            if Arr[user_row, translate] != "X":
                reservacion = fn.reservar_boleto(Arr,user_row, translate)
                imprimir = fn.imprimir_asientos(Arr)
                rueda = link.silla(silla, user_row, user_column)
            else: 
                print ("Asiento ya reservado, intentelo de nuevo")
            print (reservacion)
            contador = contador + 1
    #Random reserva solo de asientos normales
    elif opcion == 4:
        print ("\n Procesando su solicitud...")
        time.sleep(2)
        reservar_random = fn.reservar_random(Arr)
        imprimir_random = fn.imprimir_asientos(Arr)
    #Funcion para remover boleto del array
    elif opcion == 5:
        user_column = input ("Ingrese la columna que desea remover: ")
        user_row = int(input("Ingrese la fila que desea remover: "))
        silla = str(input("Necesitaba de servicios especiales? (Y/N) "))
        print ("\n Procesando su solicitud... ")
        time.sleep(2)
        translate = fn.translate_to_number(user_column)
        if silla == "Y":
            ruedo = "Y"
            remover = fn.remover_boleto(Arr, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
            imprimir_remover = fn.imprimir_asientos(Arr)
        else:
            ruedo = "N"
            remover = fn.remover_boleto(Arr, user_row, translate)
            remove_linked = link.remove(ruedo, user_row, user_column)
            imprimir_remover1 = fn.imprimir_asientos(Arr)
    elif opcion == 6:
        despegar = fn.despegar_avion()
        if despegar != None:
            print ("El avion", despegar, "se ha retirado a su destino...")
            link.empty()
            Arr = np.array( [
        ["","A","B","C","D","E","F"],
        ["1","0","0","0","0","0","0"],
        ["2","0","0","0","0","0","0"],
        ["3","0","0","0","0","0","0"],
        ["4","0","0","0","0","0","0"],
        ["5","0","0","0","0","0","0"],
        ["6","0","0","0","0","0","0"],
        ["7","0","0","0","0","0","0"],
        ["8","0","0","0","0","0","0"]
    ]) 
        else:
            print("No se encuentran aviones disponibles en espera...")


    elif opcion == 7:
        print ("Estos son los aviones que hay de momento:")
        print(stack.hangar)
        time.sleep(2)
        print("\nmoviendo avion de hangar a lista de espera...")
        time.sleep(2)
        move = fn.agregar_avion_queue()
        if move != None:
            print("el avion", move, "se ha agregado a la lista de espera")
        else:
            print("El hangar se encuentra vacio")
        print("\nHangar actualizado:")
        print (stack.stack)
    elif opcion == 8:
        opcion_rutas = int(input("""
                            1. Paris
                            2. Miami
                            3. Vancouver
        """))
        if opcion_rutas == 1:
            Ruta_francia = graf.francia()
        elif opcion_rutas == 2:
            Ruta_Miami = graf.miami()
        elif opcion_rutas == 3:
            Ruta_Vancouver = graf.canada()

    elif opcion == 9:
        Ruta = graf.rutas_areolinea()
    #Salir del menu
    elif opcion == 10:
        print ("Gracias por utilizar nuestros servicios!...")
        menu = False