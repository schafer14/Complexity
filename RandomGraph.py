from Graph import Node
from Graph import Edge
from Graph import Graph

import FIFO
import random

class RandomGraph(Graph):
	def add_random_edges(this, p):
		for n1 in this:
			for n2 in this:
				if (random.random() < p and n1 > n2):
					e = Edge(n1, n2)
					this.add_edge(e)

def test_is_connected(n, p):
	nodes = []

	for x in range(0, n):
		n = Node(x)
		nodes.append(n)

	g = RandomGraph(nodes, [])
	g1 = RandomGraph(nodes, [])
	g1.add_all_edges()
	g.add_random_edges(p)
	
	# print 'number of random edges ' + `len(g.edges())`
	# print 'number of possible edges ' + `len(g1.edges())`

	return g.is_connected()

def test_path(n, p):
	nodes = []
	for x in range(1, n):
		nodes.append(Node(x))

	g = RandomGraph(nodes, [])
	g.add_random_edges(p)


	start = g.nodes()[random.randrange(0, len(nodes) - 1)]
	dest = g.nodes()[random.randrange(0, len(nodes) - 1)]

	optDest = g.bfsOpt(start, dest)
	return g.path(optDest)
	

def main(script, *args):
	print test_path(1000, .005)

if __name__ == '__main__':
    import sys
    main(*sys.argv)