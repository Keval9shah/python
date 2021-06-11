# linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.nextNode = None


class listHead:
    def __init__(self, val):
        self.head = Node(val)
        self.count = 1

    def check(self, val):
        if isinstance(val, Node):
            nNode = val
        else:
            nNode = Node(val)
        head = self.head
        while head:
            if nNode == head:
                nNode = Node(nNode.val)
                break
            else:
                head = head.nextNode
        return nNode

    def addNode(self, val):
        head = self.head
        newNode = self.check(val)
        while head.nextNode:
            head = head.nextNode
        head.nextNode = newNode

    def insertNode(self, prevNode, val):
        newNode = self.check(val)
        newNode.nextNode = prevNode.nextNode
        prevNode.nextNode = newNode

    def insertHead(self, val):
        head = self.head
        x = self.check(val)
        x.nextNode = head
        self.head = x

    def rmvNode(self, val):
        head = self.head
        if isinstance(val, Node):
            cmp = head
        else:
            cmp = head.val
        while head.nextNode and cmp != val:
            temp = head
            head = head.nextNode
            if isinstance(val, Node):
                cmp = head
            else:
                cmp = head.val
        if head.nextNode:
            temp.nextNode = head.nextNode
        elif cmp == val:
            temp.nextNode = None
        else:
            print("There's no such Node")

    def printList(self):
        head = self.head
        if head:
            print(head.val)
        while head and head.nextNode:
            print(head.nextNode.val)
            head = head.nextNode

    def reverseList(self):
        head = self.head
        current = head
        prev = None
        while current.nextNode:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next
        current.nextNode = prev
        self.head = current


# Driver code
list = listHead(92)

# adding at end
x2 = Node(22)
x3 = Node(75)
list.addNode(x2)
list.addNode(79)
list.addNode(x3)

# inserting
list.insertNode(x2, 94)
list.insertNode(x3, 216)

# inserting at begining
list.insertHead(1000)
list.insertHead("hi")
list.insertHead(22)

# removing a node
list.rmvNode(x2)
list.printList()

print("......................")
# reverse a linked list
list.reverseList()
list.printList()
