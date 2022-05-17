import graphviz
from sympy import doctest
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
dot = graphviz.Digraph(comment = 'Flight routes')
dot  #doctest: +ELLIPSIS

dot.node  ('A', 'GUA (La aurora)')
dot.node ('B', 'PTY (Tocumen IA)')
dot.node ('L', 'PAR (Charles de Gualle')

dot.edges(['AB'])
dot.edge ('B', 'L', constraint = 'false')
 
print (dot.source)


dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
'doctest-output/round-table.gv.pdf'