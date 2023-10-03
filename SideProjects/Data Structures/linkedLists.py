class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")
node4 = linkedListNode("77")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
# node1 -> node2 -> node3
currentNode = node1
# making node1 the head
while True:
    print(currentNode.value, "->")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode
