
l = [1,2,3,4,5,6,7,8]
def recursion(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        meta = len(lista) // 2

        lista_sx = lista[:meta]
        lista_dx = lista[meta:]
        print(lista_sx, lista_dx)
        recursion(lista_sx)
        recursion(lista_dx)

if __name__ == '__main__':
    recursion(l)
