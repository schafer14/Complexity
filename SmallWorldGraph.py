from RandomGraph import RandomGraph
from Graph import Node
from Graph import Edge

import random
import math


class SmallWorldGraph(RandomGraph):
	def rewire(this, p):
		rep = int(p * len(this.edges()))
		for x in range(0, rep):
			edges = this.edges()
			nodes = this.nodes()
			e = edges[int(math.floor(random.random() * len(edges)))]
			n1, n2 = e
			this.remove_edge(e)
			r = int(random.random() * len(nodes))
			n3 = nodes[r]
			e1 = Edge(n1, n3)
			this.add_edge(e1)

def build(n):
	nodes = []
	for x in range(0, n):
		nodes.append(Node(x))
	g = SmallWorldGraph(nodes, [])
	return g

