from collections import deque
import queue as queue
from re import I
 
hangar = ["U476", "F387"]
stack = deque()

temp = ""

for i in hangar:
    temp = i
    stack.append(temp)

def stackit():

    last = stack.pop()
    queue.a_queue.enqueue(last)

    return last


 