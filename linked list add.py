class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head  
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("None") 

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:        
            self.head = new_node
            return
        temp = self.head
        while temp.next:         
            temp = temp.next
        temp.next = new_node     


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)


n1.next = n2
n2.next = n3
n3.next = n4


s1 = Single()
s1.head = n1

print("Original Linked List:")
s1.display()


s1.add_end(50)

print("After Adding 50:")
s1.display()

