
#combinazione con ordine
#2metodi


#1 con una funzione di python
from itertools import permutations

def permut(lista):
    for p in permutations(lista):
        print(list(p))

if __name__ == '__main__':
    l = ['A', 'B', 'C']
    permut(l)
    print('-----------------------------------------------')


#2 metodo ricorsivo

def permutazioni(lista, lista_parziale, usati):

    print(lista_parziale)

    for i in range(len(lista)):

        if usati[i]:
            continue

        usati[i] = True
        lista_parziale.append(lista[i])
        permutazioni(lista, lista_parziale, usati)

        lista_parziale.pop()
        usati[i] = False

if __name__ == '__main__':
    l = ['A', 'B', 'C']
    lp = []
    u = [False] * len(l)
    permutazioni(l, lp, u)
    print('-----------------------------------------------')



