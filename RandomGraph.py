from Graph import Node
from Graph import Edge
from Graph import Graph

import FIFO
import DLList
import random
import math

class RandomGraph(Graph):
	def add_random_edges(this, p):
		for n1 in this:
			for n2 in this:
				if (random.random() < p and n1 > n2):
					e = Edge(n1, n2)
					this.add_edge(e)

	def add_random_edges_fixed(this, p):
		total = len(this)
		edges = total * (total-1) / 2 * p
		edge = 0
		nodes = this.nodes()
		print edges / len(nodes) * 2
		while (edge < edges):
			r1 = nodes[int(math.floor(random.random() * total))]
			r2 = nodes[int(math.floor(random.random() * total))]
			if (r1 != r2):
				try:
					this[r1][r2]
				except:
					this.add_edge(Edge(r1, r2))
					edge = edge + 1
		return None



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
	print 'nodes made'

	g = RandomGraph(nodes, [])
	print 'nodes added'
	g.add_random_edges(p)
	print 'edges added'

	start = g.nodes()[random.randrange(0, len(nodes) - 1)]
	dest = g.nodes()[random.randrange(0, len(nodes) - 1)]

	optDest = g.bfsOpt(start, dest)
	return g.path(optDest)

def test_dll():
	n = 10
	dllist = DLList.DLList()
	iter = {Node(x) for x in range(1, n)}
	for x in iter:
		dllist.append(x)


def build(n):
	nodes = []
	for x in range(1, n):
		nodes.append(Node(x))
	g = RandomGraph(nodes, [])
	return g

def main(script, *args):
	test_dll()
	
	

if __name__ == '__main__':
    import sys
    main(*sys.argv)