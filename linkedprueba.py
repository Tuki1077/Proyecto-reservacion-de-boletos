class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

    def pop_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None 

#linkedList
llist = LinkedList()
print(llist)



def silla(rueda ,user_row ,user_column):
    if rueda == "si":
        esto = "!" + user_column + str(user_row)
        #add first

        llist.add_first(Node(esto))
        print(llist)

    elif rueda == "no":
        esto = user_column + str(user_row)
        #add last

        llist.add_last(Node(esto))
        print(llist)
    else:
        print("Ingrese si o no.")

def remove(ruedo, user_row, user_column):
    if ruedo == "si":
        estos = "!" + user_column + str(user_row)
        llist.remove_node(estos)
        print(llist)

    elif ruedo == "no":
        estos = user_column + str(user_row)
        llist.remove_node(estos)
        print(llist)