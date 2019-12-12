class Node:
	data = ""
	root = None
	nextNode = None
	lastNode = None

	def __init__(self, data):
		self.data = data

#think book stack
class Stack:
	
	root = None
	length = 0

	def __init__(self):
		pass

	def addNode(self, name):
		counter = 0
		node = Node(name)
		if self.root == None:
			self.root = node
			self.lastNode = node
			self.length = 1
		else:
			self.lastNode.nextNode = node
			self.lastNode = node
			self.length = self.length + 1

	def pop(self):
		self.lastNode = None
		self.length = self.length - 1

	def printList(self):
		current = self.root
		counter = 0
		while counter < self.length:
			print(current.data)
			counter = counter + 1
			current = current.nextNode

	def getLength(self):
		return self.length
