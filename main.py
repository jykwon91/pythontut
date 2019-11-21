from SingleLinkedList import SingleLinkedList
from Stack import Stack
from Queue import Queue
from HashMap import HashMap

list = SingleLinkedList()
list.addNode("Jason")
list.addNode("Tristan")
list.addNode("Albert")
list.addNode("Jax")
list.printList()

print("******stack********")
stack = Stack()
stack.addNode("Jason")
stack.addNode("Tristan")
stack.addNode("Albert")
stack.addNode("Jax")
stack.printList()
stack.pop()
print("**pop**")
stack.printList()

print("*******queue********")
queue = Queue()
queue.addNode("Jason")
queue.addNode("Tristan")
queue.addNode("Albert")
queue.addNode("Jax")
queue.printList()
print("**pop**")
queue.queuePop()
queue.printList()

print("*****hash map******")
hashmap = HashMap()
