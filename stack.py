from asyncio.windows_events import NULL
from collections import deque
import queue as queue
from re import I
 
hangar = ["U476", "F387", "P231", "H312", "D201"]
stack = deque()

temp = ""

for i in hangar:
    temp = i
    stack.append(temp)

def stackit():
    if len(stack) != 0:
        last = stack.pop()
        queue.a_queue.enqueue(last)

        return last
    else:
        return None