class Node:

    def __init__(self, data = None, next = None):
        # When create node, the node could have no data and next node
        # but we'd better to have value for the node and next node
        self.data = data
        self.next_node = next



class LinkedList:
    def __init__(self, first_node = None):
        self.first_node = first_node

    def read(self, index):
        # read a linkedlist has to be from very first place
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:  # current_node is none
                return None

        return current_node.data



def main():
    node_1 = Node("Once")  
    node_2 = Node("upon") 
    node_3 = Node("a")    
    node_4 = Node("time") 

    node_1.next_node = node_2
    node_2.next_node = node_3 
    node_3.next_node = node_4 

    list = LinkedList(node_1)

    print(list.read(3))

main()