import numpy as np
import functions as fn
import linkedprueba as link
import stack as stack
import time 
import grafo as graf
import random

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
# menu = True
# while menu == True:
print ("""
                        1. Ver disponibilidad de boletos                 6. Despegar avion
                        2. Ver asientos ya reservados                    7. Agregar avion de hangar a lista de espera
                        3. Reservar boleto de forma manual               8. Ver Rutas del Dia
                        4. Reserva boleto aleatoriamente                 9. Ver rutas de aerolinea 
                        5. Desocupar asiento                             10. Salir
""")
opcion = 3
opcion2 = 4
opcion3 = 5
Column = ["A","B","C","D","E","F"]
row = [1,2,3,4,5,6,7,8]
si_usa = ["Y", "N"]

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
    y = random.randint(1,20)
    contador = 0

    while contador < y:
        user_column = random.choice(Column)
        user_row = random.choice(row)
        silla = random.choice(si_usa)
        print ("\n Procesando su solicitud... ")
        translate = fn.translate_to_number(user_column)
        if Arr[user_row, translate] != "X":
            reservacion = fn.reservar_boleto(Arr,user_row, translate)
            imprimir = fn.imprimir_asientos(Arr)
            rueda = link.silla(silla, user_row, user_column)
        else: 
            print ("Asiento ya reservado, intentelo de nuevo")
        print (reservacion)
        contador = contador + 1
elif opcion == 4:
        print ("\n Procesando su solicitud...")
        reservar_random = fn.reservar_random(Arr)
        imprimir_random = fn.imprimir_asientos(Arr)
elif opcion3 == 5:
        user_column = random.choice(Column)
        user_row = random.choice(row)
        silla = random.choice(si_usa)
        print ("\n Procesando su solicitud... ")
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