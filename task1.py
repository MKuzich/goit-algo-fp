import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self, msg):
        current = self.head
        arr = []
        while current:
            arr.append(current.data)
            current = current.next
        print(msg, ': ', arr)

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
    
    def sort(self):
        if not self.head:
            return
        cur = self.head
        while cur.next:
            if cur.data > cur.next.data:
                cur.data, cur.next.data = cur.next.data, cur.data
                cur = self.head
            else:
                cur = cur.next
                
    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return

        cur1 = self.head
        cur2 = other.head

        if cur1.data > cur2.data:
            cur1, cur2 = cur2, cur1
            self.head = cur1

        while cur1.next and cur2:
            if cur1.next.data > cur2.data:
                temp = cur1.next
                cur1.next = cur2
                cur2 = temp
            cur1 = cur1.next
        if cur2:
            cur1.next = cur2


def create_linked_list():
    ll = LinkedList()
    for _ in range(10):
        ll.add(random.randint(1, 100))
    return ll

ll1 = create_linked_list()
ll2 = create_linked_list()


ll1.print_list('Згенерований список 1')
ll1.sort()
ll1.print_list('Відсортований список 1')
ll1.reverse()
ll1.print_list('Реверсований список 1')
ll2.print_list('Згенерований список 2')
ll1.sort()
ll2.sort()
ll1.merge(ll2)
ll1.print_list('Об\'єднаний список')