from pydoc import doc


class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

    #Creacion del queue
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        #funcion que hace queue un nodo en la lista
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        #funcion que quita el nodo del queue
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
 
#aqui hacemos queue los avines al queue listos para ser usados
a_queue = Queue()

a_queue.enqueue("A155")
a_queue.enqueue("B453")
a_queue.enqueue("J783")
