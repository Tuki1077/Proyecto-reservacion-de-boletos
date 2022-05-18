import graphviz
from sympy import doctest
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
dot = graphviz.Digraph(comment = 'Flight routes')

#Aqui definimos el grafo con ruta a Paris, Francia
def francia():
    dot.node  ('A', 'GUA (La aurora)')
    dot.node ('B', 'PTY (Tocumen IA)')
    dot.node ('L', 'PAR (Charles de Gualle)')

    dot.edges(['AB'])
    dot.edge ('B', 'L', constraint = 'false')
    
    print (dot.source)


    dot.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'

#Aqui definimos el grafo con ruta a Miami, USA
def miami():
    dot.node  ('J', 'GUA (La aurora)')
    dot.node ('M', 'MIA (Miami IA)')

    dot.edges(['JM'])
    
    print (dot.source)


    dot.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'

#Aqui definimos el grafo con ruta a Vancouver, Canada
def canada():
    dot.node ('V', 'YVR (Vancouver IA)')
    dot.node ('S', 'SFO (San Franciso IA')
    dot.node  ('G', 'GUA (La aurora)')

    dot.edge ('S', 'V')
    dot.edge ('G', 'S')
    
    print (dot.source)


#render el pdf de los grafos
    dot.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'
