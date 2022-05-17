from asyncio.windows_events import NULL
from collections import deque
import queue as queue
from re import I
 
 #array donde le manda informacion al stack 1 por 1
hangar = ["U476", "F387", "P231", "H312", "D201"]
#Create el stack
stack = deque()

temp = ""

for i in hangar:
    temp = i
    stack.append(temp)

#sacar el el ultimo avion en entrar al hangar y mandarlo al ultimo lugar de la lista de espera
def stackit():
    if len(stack) != 0:
        last = stack.pop()
        queue.a_queue.enqueue(last)

        return last
    else:
        return None