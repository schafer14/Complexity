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

	#returns all the edges in a graph
	def edges(this):
		l = []
		for n1 in this:
			for n2 in this[n1]:
				try:
					l.index(this[n1][n2])
				except:
					l.append(this[n1][n2])
		return l
	
	# returns a list of nodes adjacent to a node
	def out_nodes(this, node):
		return this[node].keys()

	# returns all edges attached to a node
	def out_edges(this, node):
		l = []
		for n2 in this[node]:
			l.append(this[node][n2])
		return l

	# makes a complete graph by adding edges to an edgless graph
	def add_all_edges(this):
		for n1 in this:
			for n2 in this:
				if (n1 != n2):
					e = Edge(n1, n2)
					this.add_edge(e)

	# Adds edges till graph is regular at number n
	def add_regular_edges(this, num):
		for n1 in this:
			for n2 in this:
				if (this.out_edges(n1).__len__() <= num
					and this.out_edges(n2).__len__() <= num):
					e = Edge(n1, n2)
					this.add_edge(e)

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

# Inherits from object class
class Node(object):
	def __init__(self, label=''):
		self.label = label

	# repr retruns a string repersentation of the node object
	def __repr__(self):
		return 'Node (%s)' % repr(self.label)

	# returns a human readable version of repr (Helpful with more attrs)
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

    e = Edge(v, w)
    e1 = Edge(w, x)
    e2 = Edge(w, z)
    e3 = Edge(z, y)

    g = Graph([v,w,x,y,z], [e,e1,e2,e3])

    print g.is_connected()
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)