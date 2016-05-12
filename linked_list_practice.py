class Node: 
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList: 
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(value):
		node = Node(value)
		if self.head == None
			self.head = node
			self.tail = node
		else: 
			self.tail.next=node
			self.tail = node

	def removeNode(self, node_value):
		#removes first node taht ha same value as given node_value
		current = self.head
		if current.value == node_value::
			self.head = self.head.next
		while (current.next != None):
			if current.next.value == node_value
				current.next = current.next.next
				break
			else:
				current = current.next

	