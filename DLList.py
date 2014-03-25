class DLList(object):
	def __init__(self, nl=[]):
		self.nl = nl
		self.last = None
		self.first = None

	def __str__(self):
		return str(self.nl)

	def __len__(self):
		return len(self.nl)

	def append(self, node):
		if(len(self) > 0):
			try:
				node.prev = self.last
				self.last.next = node
				self.last = node
			except:
				node
		else:
			self.first = node
			node.next = None
		self.nl.append(node)

	def pop(self):
		try:
			self.nl[0].pn = None
		except:
			raise
		return self.nl.pop(0)