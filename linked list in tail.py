class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("None")

    
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    
    def get_nth_from_tail(self, n):
        length = self.count_nodes()
        if n > length or n <= 0:
            return None  
        pos_from_head = length - n + 1
        temp = self.head
        count = 1
        while temp:
            if count == pos_from_head:
                return temp.data
            temp = temp.next
            count += 1
        return None


s1 = Single()
for val in [10, 20, 30, 40, 50]:
    s1.add_end(val)

print("Linked List:")
s1.display()

n = 3
result = s1.get_nth_from_tail(n)
if result is not None:
    print(f"Data at {n}th node from tail is:", result)
else:
    print(f"Position {n} is out of range")
