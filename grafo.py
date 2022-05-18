import graphviz
from sympy import doctest
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
dot = graphviz.Digraph(comment = 'Flight routes')
dot1 = graphviz.Digraph(comment = 'Flight routes')
dot2 = graphviz.Digraph(comment = 'Flight routes')

def francia():
    dot.node  ('A', 'GUA (La aurora)')
    dot.node ('B', 'PTY (Tocumen IA)')
    dot.node ('L', 'PAR (Charles de Gualle)')

    dot.edges(['AB'])
    dot.edge ('B', 'L', constraint = 'false')
    
    print (dot.source)


    dot.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'

def miami():
    dot1.node  ('J', 'GUA (La aurora)')
    dot1.node ('M', 'MIA (Miami IA)')

    dot1.edges(['JM'])
    
    print (dot1.source)


    dot1.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'

def canada():
    dot2.node ('V', 'YVR (Vancouver IA)')
    dot2.node ('S', 'SFO (San Franciso IA')
    dot2.node  ('G', 'GUA (La aurora)')

    dot2.edge ('S', 'V')
    dot2.edge ('G', 'S')
    
    print (dot2.source)


    dot.render('doctest-output/Flights-routes.gv', view=True)  # doctest: +SKIP
    'doctest-output/Flight-routes.gv.pdf'
