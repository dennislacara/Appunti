import networkx as nx

g = nx.Graph()

g.add_node('A')
g.add_node('B')

g.add_edge('A', 'B', weight=0, indice = 0)

print(g.edges)
if ('B','A') in g.edges(('B','A')):
    print(True)
else:
    print(False)

for i in range(0, 10):
    print(f"aggiungo {20} e incremento l'indice di 1")

    g['B']['A']['weight'] +=20
    print(g['B']['A'])
    print(g['A']['B'])
    print()

for edge in g.edges(data=True):
    print(edge)

print(g.nodes())


