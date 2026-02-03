import networkx as nx

g = nx.DiGraph()
elementi = ['A', 'B', 'C', 'D', 'E', 'F']
connessioni = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('C', 'F'), ('F', 'K'), ('E', 'J'), ('J','L'), ('6','7')]
g.add_edges_from(connessioni)
print(0, g)
    # F K
# A B C
     #D E J L

#alcune funzioni nx riguardo la 'deep first search'

#NX.DFS_TREE : Restituisce un grafo con tutti i nodi raggiungibili a partire da source
#NB: se il grafo è orientato, la funzione considera il verso di percorrenza
#NB: il risultato comprende anche il nodo di partenza (eventualmente da escludere con un if)
f1 = nx.dfs_tree(g, source='B')
print(1, f1)

#NX.DFS_EDGES : restituisce gli archi che vengono incontrati nel percorso a partire da source
#NB: funzione che restituisce un iteratore da convertire in lista
f2 = list(nx.dfs_edges(g, source='C'))
print(2, f2)

#DFS_SUCCESSORS: stampa un dizionario in ordine gerarchico dei nodi percorsi
f3 = nx.dfs_successors(g, source='A')
print(3, f3)
#al contrario, DFS_PREDECESSORS

#EDGE_DFS
f4 = list(nx.edge_dfs(g, source='C'))
print(4, f4)

#IS_CONNECTED: si tratta di una funzione ch verifica che un grafo sia connesso. Ritorna un valore bool.
f5 = nx.is_strongly_connected(g) #per grafi orientati
#f5 = nx.is_connected(g)
print(5, f5)

# NODE_CONNECTED_COMPONENT : ritorna un insieme costituito dai nodi della componente connessa
# a cui appartiene n ( n compreso, quindi bisgona usare un if)
#f6 = nx.node_connected_component(g,'6') #solo per grafi non orientati
#print(6, f6)

#CONNECTED_COMPONENTS: restituisce una lista di insiemi, in cui ogni insieme rappresenta una componente connessa
# NB: restituisce un iteratore; inoltre se si vuole conoscere il num di comp.conn. -> len(f7)
#f7 = list(nx.connected_components(g))
f7 = nx.strongly_connected_components(g) #grafi orientati

print(7, f7)

#HAS_PATH : restituisce un valore bool, in base all'esistenza di un percorso source->target
f8 = nx.has_path(g, source='A', target='B')
print(8, f8)

#IS_PATH: restituisce un valore bool, in base all'esistenza di un percorso espresso come lista
f9 = nx.is_path(g, ['A', 'B', 'C', 'D', 'E', 'F'])
print(9, f9)

# DESCENDENTS: tutti i nodi raggiungibili partendo da source
f10 = nx.descendants(g, 'A')
print(10, f10)

#NEIGHBORS: restituisce l'iteratore di vicini di un nodo (arche orientato)
f11 = list(nx.neighbors(g, 'B'))
print(11, f11)

#TO_UNDIRECTED: trasforma un grafo orientato in un grafo non orientato
f12 = nx.to_undirected(g).copy()
print(12, f12)


# grafo.SUCCESSORS(nodo) o grafo.PREDECESSORS(nodo) : restituiscono iteratori che contengono i nodi succ/predec
# che circondano il nodo inserito come argomento. (utile per grafi orientati)
f13 = list(g.successors('A'))
f14 = list(g.predecessors('B'))
print(13, f13)
print(14, f14)


#Grafo.out_edges(nodo) o Grafo.in_edges(nodo) restituiscono iteratori che contengono i nodi che circondano il nodo inserito come argomento.
g.out_edges('A', data=True) #Restituisce tutti gli archi uscenti dal nodo 'A'
g.in_edges('B', data=True) #Restituisce tutti gli archi entranti nel nodo 'B'


