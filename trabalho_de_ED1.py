class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
            return

        if data < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


if __name__ == "__main__":
    pares = SinglyLinkedList()
    impares = SinglyLinkedList()

    print("Digite 20 números inteiros:")
    for i in range(20):
        num = int(input(f"Número {i+1}: "))
        if num % 2 == 0:
            pares.insert_end(num)
        else:
            impares.insert_end(num)

    ordenada = DoublyLinkedList()

    for num in pares.to_list() + impares.to_list():
        ordenada.insert_sorted(num)

    print("\nLista ordenada crescente:")
    ordenada.display_forward()

    print("Lista ordenada decrescente:")
    ordenada.display_backward()
