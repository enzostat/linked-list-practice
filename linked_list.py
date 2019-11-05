class Node:
    def __init__(self, data):
        self.data = data #a Node w/ a given data property
        self.next = None #a Node also has a .next property initialized to None
        # pass
        # a Node starts with a given data property
        # a Node also has a .next property initialized as null

node1 = Node(123)
print(node1.data)


    

class LinkedList:
    def __init__(self):
        self.head = None # a Linked List starts with a "head" property intialized as null
    
    def addNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # creates a new node with the given data and adds it to the front of the list
    
    def pop(self):
        pass
        # removes the last node from the list and returns it
    
    def removeFromFront(self):
        pass
        # remove the head node from the list and return it
        # the next node in the list is the new head node
    
    def insertAt(self, X, data):
        new_node = Node(data)
        if X == 0 or self.head == None:
            self.addNode(data)
            return
        prev = None
        current = self.head
        count = 0

        while current != None:
            count += 1
            prev = current
            current - current.next

            if count == X:
                prev.next = new_node
                new_node.next = current
                return new_node
        
        new_node.next = None
        prev.next = new_node
        # insert a new node into the list with the given data
        # place it after X nodes in the list
        # if X exceeds the bounds of the list, put the node at the end
        # insertAt(0, 7) would add the new node as the head
    
    def removeAt(self, X):
        if self.head == None:
            return False
        if X == 0:
            removed_node = self.head
            self.head = self.head.next
            return removed_node
        


        prev = None
        current = self.head
        currentIdx = 0
        while current.next != None and currentIdx < X:
            prev = current
            current = current.next
            currentIdx += 1
        
        prev.next = current.next

        return current
        # currentNode.next = None
        # remove the Xth node from the list, considering 0 to be the first node
        # return the node that has been removed
    
    def search(self, data):
        prev = None
        current = self.head
        i = 0

        while current != None:
            if current.data == data:
                print(f"Data was found at node: {i}")
                return i
            else:
                i+= 1
                prev = current
                current = current.next
            
        
        # searches the list for a node with the given data
        # if it is found, return the "index" of the node, considering 0 to be the first node
        # if not, return false
    
    def sort(self):
        current = self.head

        while current != None:
            current = current.next
        # sort the Linked List in ascending order of data values


llist = LinkedList()
llist.addNode(5)
llist.addNode(6)
llist.addNode(7)
llist.addNode("Twelve")
