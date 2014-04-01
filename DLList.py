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
			self.last = node
			node.next = None
		self.nl.append(node)

	def pop(self):
		ret = self.first
		try:
			self.first = ret.next
			self.nl.pop(0)
		except:
			self.nl.pop(0)
		return ret