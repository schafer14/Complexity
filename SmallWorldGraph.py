from RandomGraph import RandomGraph
from Graph import Node
from Graph import Edge

import DLList
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
		return rep

	def label(this, node=0):
		if node == 0:
			node = this.nodes()[0]
		g.home = node
		node.d = 0
		queue = DLList.DLList()
		queue.append(node)
		while (len(queue) > 0):
			n1 = queue.pop()
			for n2 in this.out_nodes(n1):
				if not hasattr(n2, 'd'):
					n2.d = n1.d + 1
					queue.append(n2)

	def dist(this):
		for node in this.nodes():
			print 'Node: ' + `node` + ' is ' + `node.d` + ' hops from ' + `g.home`

	def avgd(this):
		d = 0.0
		for node in this.nodes():
			d = d + node.d
		return d / len(this.nodes())

def build(n):
	nodes = []
	for x in range(0, n):
		nodes.append(Node(x))
	g = SmallWorldGraph(nodes, [])
	return g


g = build(1000)
print `g.add_regular_edges(5)` + ' total edges'
print `g.rewire(.1)` + ' edges rewired.' 
g.label()
print `g.avgd()` + ' average distance.'