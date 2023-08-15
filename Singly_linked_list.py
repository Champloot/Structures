class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"[{self.data}]->{self.next}"


class LinkedList:
    def __int__(self, head=None):
        self.head = head

    def __str__(self):
        return f"{self.head}"

    def getSize(self):
        temp = self.head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt

    def addNodeHead(self, data):
        node = Node(data, self.head)
        self.head = node
        return "Successfully added"

    def addNodeTail(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return "Successfully added"

linked_list = LinkedList()
linked_list.head = Node(1)
print(linked_list)
print(linked_list.getSize())

linked_list.addNodeHead(0)
print(linked_list)
print(linked_list.getSize())

linked_list.addNodeTail(2)
print(linked_list)
print(linked_list.getSize())
