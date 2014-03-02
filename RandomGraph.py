from Graph import Node
from Graph import Edge
from Graph import Graph

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
	g.add_random_edges(p)

	return g.is_connected()

def main(script, *args):
	for n in range(997, 1000):
		for t in range(1, 100):
			p = float(t / 100.0)
			if not test(n, p):
				print '(' + `n` + ', ' + `p` + ')'

if __name__ == '__main__':
    import sys
    main(*sys.argv)