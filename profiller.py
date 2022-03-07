import cProfile 
import functions as func
import numpy as np

Avion = np.array( [
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
# Avion_con_asiento_reservado = np.array ( [
#     ["","A","B","C","D","E","F"],
#     ["1","X","0","0","0","0","0"],
#     ["2","0","0","0","0","0","0"],
#     ["3","0","0","0","0","0","0"],
#     ["4","0","0","0","0","0","0"],
#     ["5","0","0","0","0","0","0"],
#     ["6","0","0","0","0","0","0"],
#     ["7","0","0","0","0","0","0"],
#     ["8","0","0","0","0","0","0"]
# ])
letra = "D"

cProfile.run("func.reservar_boleto(Avion, 1, 1)")
cProfile.run("func.translate_to_number(letra)")
cProfile.run("func.reservar_random(Avion)")
# cProfile.run("func.remover_boleto(Avion_con_asiento_reservado,1,1)")