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


def main(script, *args):
    v = Node('v')
    w = Node('w')
    x = Node('x')
    y = Node('y')
    z = Node('z')
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    e = Edge(v, w)
    e1 = Edge(w, x)

    g = RandomGraph([v,w,x,y,z,a,b,c,d,e], [])
    
    g.add_random_edges(.5)
    print len(g.edges())

if __name__ == '__main__':
    import sys
    main(*sys.argv)