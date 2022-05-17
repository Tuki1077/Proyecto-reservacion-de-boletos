import numpy as np
import functions as fn
import linkedprueba as link
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
                            1. Ver disponibilidad de boletos
                            2. Reservar boleto de forma manual
                            3. Reserva boleto aleatoriamente
                            4. Desocupar asiento
                            5. Despegar avion
                            6. Agregar avion de hangar a lista de espera
                            7. Ver Rutas del Dia
                            8. Salir
    """)
    opcion = int(input())
    #imprimir array
    if opcion == 1:
        for i in Arr:
            print('\t'.join(map(str, i)))
        print (link.llist)
        #reserva de asientos ya sea silla de ruedas o normal
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
            if Arr[user_row, translate] != "X":
                reservacion = fn.reservar_boleto(Arr,user_row, translate)
                imprimir = fn.imprimir_asientos(Arr)
                rueda = link.silla(silla, user_row, user_column)
            else: 
                print ("Asiento ya reservado, intentelo de nuevo")
            print (reservacion)
            contador = contador + 1
    #Random reserva solo de asientos normales
    elif opcion == 3:
        print ("\n Procesando su solicitud...")
        time.sleep(2)
        reservar_random = fn.reservar_random(Arr)
        imprimir_random = fn.imprimir_asientos(Arr)
    #Funcion para remover boleto del array
    elif opcion == 4:
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
    elif opcion == 5:
        despegar = fn.despegar_avion()
        if despegar != None:
            print ("El avion", despegar, "a despegado...")
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


    elif opcion == 6:
        print("moviendo avion de hangar a lista de espera...")
        move = fn.agregar_avion_queue()
        if move != None:
            print("el avion", move, "se ha agregado a la lista de espera")
        else:
            print("El hangar se encuentra vacio")
    elif opcion == 7:
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


    #Salir del menu
    elif opcion == 8:
        print ("Gracias por utilizar nuestros servicios!...")
        menu = False