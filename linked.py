class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def get_contents(self):
		return self.data

	def __repr__(self):
		return "<Node Object: "+str(self.data)+" | "+str(self.next)+">"

class LinkedList:
	def __init__(self):
		self.last_node = None
		self.first_node = None

	def add_node(self, data):
		new_node = Node(data = data)

		if self.first_node == None:
			self.first_node = new_node
			self.last_node = new_node

		self.last_node.next = new_node
		self.last_node = new_node

		return new_node

	def insert_node_after(self, search, data):
		node = self.first_node

		if node.get_contents() == search:
			node.next = Node(data = data, next = node.next)
			return

		while node:
			if node.next != None and node.next.get_contents() == search:
				node.next = Node(data = data, next = node.next)
				return

			node = node.next

	def print_list(self, node = None):
		if node == None:
			node = self.first_node

		while node:
			print node.get_contents()
			node = node.next

		print ""

	def delete_node(self, search):
		node = self.first_node

		if node.get_contents() == search:
			node = node.next
			return

		while node:
			if node.next != None and node.next.get_contents() == search:
				node.next = node.next.next
				return

			node = node.next

ll = LinkedList()

ll.add_node("a")
n2 = ll.add_node("b")
ll.add_node("c")

ll.print_list()

ll.print_list(n2)

ll.insert_node_after("b", "d")

ll.print_list()

ll.delete_node("b")

ll.print_list()