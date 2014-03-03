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

def test(n, p):
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

def main(script, *args):
	nodes = []
	for n in range(1, 100):
		nodes.append(Node(n))

	g = RandomGraph(nodes, [])
	g.add_random_edges(.01)


	start = g.nodes()[random.randrange(0, len(nodes) - 1)]
	dest = g.nodes()[random.randrange(0, len(nodes) - 1)]

	print 'from ' + `start` + ' to ' + `dest`
	g.bfs(start, dest)

if __name__ == '__main__':
    import sys
    main(*sys.argv)