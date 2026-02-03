# Questo algoritmo di ricorsione genera tutte le combinazioni possibili, trascurando l'ordine;
#output:
'''

[]
['A']
['A', 'B']
['A', 'B', 'C']
['A', 'C']
['B']
['B', 'C']
['C']

'''

def _ricorsione(start_index, lista, lista_parziale):

    print(lista_parziale)

    for i in range(start_index, len(lista)):

        # scelte
        lista_parziale.append(lista[i])

        _ricorsione(i+1,lista,lista_parziale)

        lista_parziale.pop()


if __name__ == '__main__':
    l = ['A', 'B', 'C']

    _ricorsione(0, l, [])

if __name__ == '__main__':
    l = [1,2,3,4]
    v = []
    i = 0
    _ricorsione(i, l, v)
