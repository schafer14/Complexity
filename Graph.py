# Graph inherits from builtin type dinc -> for dictionary
class Graph(dict):
	def __init__(self, nodes=[], edges=[]):
		# create a new graph
		for node in nodes:
			self.add_node(node)

		for edge in edges:
			self.add_edge(edge)

	def add_node(self, node):
		# add node to the graph
		self[node] = {}

	def add_edge(self, edge):
		# add edge to the graph
		v, w = edge
		self[v][w] = edge
		self[w][v] = edge

	# returns the edge between two nodes if it exists
	def get_edge(this, n1, n2):
		try:
			return this[n1][n2]
		except:
			return 

	# removes all references to an edge from the graph
	def remove_edge(this, edge):
		del this[edge[0]][edge[1]]
		del this[edge[1]][edge[0]]

	# returns a list of nodes in a graph
	def nodes(this):
		return this.keys()

	# list comprehension of edges
	def edges(this):
		return [Edge(n1, n2) for n1 in this for n2 in this[n1] if n2 in this[n1] and n1 < n2]
	
	
	# returns a list of nodes adjacent to a node
	def out_nodes(this, node):
		return this[node].keys()

	# returns all edges attached to a node
	def out_edges(this, node):
		l = []
		for n2 in this[node]:
			l.append(this[node][n2])
		return l

	# returns all edges attached to a node using list comprehension
	def out_edges_comp(this, node):
		return [Edge(node, n2) for n2 in this[node]]

	# makes a complete graph by adding edges to an edgless graph
	def add_all_edges(this):
		for n1 in this:
			for n2 in this:
				if (n1 != n2):
					e = Edge(n1, n2)
					this.add_edge(e)

	# makes a complete graph using list comprehensions
	def add_all_edges_comp(this):
		edges = [Edge(n1, n2) for n1 in this for n2 in this if n1 is not n2]
		for e in edges:
			this.add_edge(e)

	# Adds edges till graph is regular at number n
	def add_regular_edges(self, k=2):
		vs = self.nodes()
		if k >= len(vs):
			raise ValueError, ("cannot build a regular graph with " +
				"degree >= number of vertices.")

		if k % 2 == 1:
			if (len(vs) % 2 == 1):
				raise ValueError, ("cannot build a regular graph with " +
									"an odd degree and an odd number of " +
									"vertices.")
			self.add_regular_edges_even(k-1)
			self.add_regular_edges_odd()
		else:
			self.add_regular_edges_even(k)
		return len(self.edges())

	def add_regular_edges_even(self, k=2):
		vs = self.nodes()
		double = vs * 2

		for i, v in enumerate(vs):
			for j in range(1,k/2+1):
				w = double[i+j]
				self.add_edge(Edge(v, w))

	def add_regular_edges_odd(self):
		vs = self.nodes()
		n = len(vs)
		reduplicated_list = vs * 2
		for i in range(n/2):
			v = reduplicated_list[i]
			w = reduplicated_list[i+n/2]
			self.add_edge(Edge(v, w))

	#returns all nodes with fewer then n edges
	def find_nodes(this, num):
		return [n for n in this if len(this.out_edges_comp(n)) <= num]

	# Returns true if graph is connected
	def is_connected(this):
		checked = []
		queue = []
		queue.append(this.nodes()[0])
		while (len(queue) > 0):
			for node in this.out_nodes(queue[0]):
				try:
					queue.index(node)
				except:
					try:
						checked.index(node)
					except:
						queue.append(node)
			checked.append(queue[0])
			queue.pop(0)
		return len(checked) == len(this.nodes())

	def bfs(this, start, dest):
		visited = []
		queue  = []
		queue.append(start)
		while len(queue):
			n = queue.pop()
			if (n == dest):
				return n
			for n2 in this.out_nodes(n):
				if (n2 not in visited and n2 not in queue):
					n2.parent = n
					queue.append(n2)
			visited.append(n)

	def bfsOpt(this, start, dest):
		visited = []
		queue  = []
		size = len(this)
		dest.distFromStart = size
		dest.parent = 0
		solution = dest
		start.distFromStart = 0
		queue.append(start)
		while len(queue):
			n = queue.pop()
			if (n == dest):
				if (n.distFromStart < solution.distFromStart):
					print
					solution = n
			else:
				for n2 in this.out_nodes(n):
					if (n2 not in visited and n2 not in queue):
						n2.parent = n
						n2.distFromStart = n.distFromStart + 1
						queue.append(n2)
				visited.append(n)
		if (solution.distFromStart == size):
			print 'not connected'
			return
		return solution

	def path(this, node):
		path = []
		while (hasattr(node, 'parent')):
			path.insert(0, Edge(node.parent, node))
			node = node.parent
		return path
			

# Inherits from object class
class Node(object):
	def __init__(self, label=''):
		self.label = label

	# repr retruns a string repersentation of the node object
	def __repr__(self):
		return 'Node (%s)' % repr(self.label)

	__str__ = __repr__


# Inherits from tuple class
# Immutable class
class Edge(tuple):
	# override on builtin new for tuple class
	def __new__(cls, e1, e2):
		return tuple.__new__(cls, (e1, e2))

	def __repr__(self):
		# print the repersentation of each node
		return 'Edge (%s, %s)' % (repr(self[0]), repr(self[1]))

	__str__ = __repr__

def main(script, *args):
    v = Node('v')
    w = Node('w')
    x = Node('x')
    y = Node('y')
    z = Node('z')
    a = Node('a')

    
    g = Graph([v,w,x,y,z,a], [])

    g.add_regular_edges(5)
    print g

if __name__ == '__main__':
    import sys
    main(*sys.argv)