

# aba, oro, abba
def isPalindrome(stringa):
    if len(stringa) == 0:
        return True
    elif len(stringa) == 1:
        return True
    elif len(stringa) == 2:
        return stringa[0] == stringa[1]
    else:
        return isPalindrome(stringa[1:len(stringa)-1]) if stringa[0] == stringa[-1] else False


if __name__ == '__main__':
    print(isPalindrome('aba'))

#del prof
def isP(stringa):
    if len(stringa) == 1:
        return True
    else:
        return stringa[0] == stringa[-1] and isP(stringa[1:-1])

#if __name__ == '__main__':
    print(isP('aaaa'))


def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]

        minori = []
        uguali = []
        maggiori = []

        for i in range(len(lista)):

            if lista[i] < pivot:
                minori.append(lista[i])
            elif pivot == lista[i]:
                uguali.append(lista[i])
            elif lista[i] > pivot:
                maggiori.append(lista[i])

        return quickSort(minori) + uguali + quickSort(maggiori)

#if __name__ == '__main__':
    l = [4, 7,6,5,4,3,2,8,9,10]
    print(quickSort(l))


def searchElement(lista, elemento):
    if len(lista) == 1:
        return lista[0] == elemento
    else:
        meta = len(lista) // 2

        l_sx = lista[:meta]
        l_dx = lista[meta:]

        return searchElement(l_sx, elemento) or searchElement(l_dx, elemento)

#if __name__ == '__main__':
    l = [4, 7, 6, 5, 4, 3, 2, 8, 9, 10]
    print(searchElement(l, 11))



