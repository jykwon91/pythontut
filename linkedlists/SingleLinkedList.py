class Node:
	data = ""
	nextNode = None

	def __init__(self, data):
		self.data = data

#think monkey toy
class SingleLinkedList:
	#stack: last
	#queue: first, last
	#tree: left, right

	root = None
	current = None
	length = 0
	def __init__(self):
		pass
	def addNode(self, name):
		counter = 0
		node = Node(name)
		if self.root == None:
			self.root = node
			self.length = 1
		else:
			current = self.root
			while current != None:
				counter = counter + 1
				if current.nextNode != None:
					current = current.nextNode
				else:
					current.nextNode = node
					counter = counter + 1
					current = None
			self.length = counter

	def printList(self):
		current = self.root
		counter = 0
		while counter < self.length:
			print(current.data)
			counter = counter + 1
			current = current.nextNode
			
	def getLength(self):
		return self.length
