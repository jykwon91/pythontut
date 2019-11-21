class Node:
	data = ""
	root = None
	lastNode = None
	nextNode = None

	def __init__(self, data):
		self.data = data

class Queue:

	root = None
	length = 0
	def __init__(self):
		pass

	def addNode(self, name):
		node = Node(name)
		if self.root == None:
			self.root = node
			self.lastNode = node
			self.length = 1
		else:
			self.lastNode.nextNode = node
			self.lastNode = node
			self.length = self.length + 1

	def queuePop(self):
		self.root = self.root.nextNode
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
