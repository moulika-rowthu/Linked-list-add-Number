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
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

s1 = Single()
s1.add_end(10)
s1.add_end(20)
s1.add_end(30)
s1.add_end(40)

print("Linked List:")
s1.display()

print("Number of nodes in linked list:", s1.count_nodes())
