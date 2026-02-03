# Comprensione di dataclass, property ed ereditarietà

from dataclasses import dataclass

@dataclass(order=True, eq=True) #inizializza i metodi dunder ln e eq, e confronta i primi attributi della classe
class Category:
    id: int #1
    tipo : str #2

    #attributi di istanza
    _noleggio: bool = False #attributo privato #3
    km : float = 0 #4

    #attributo di classe
    category_name = 'categoria automobili'

    def __str__(self):
        return f'{self.category_name}, {self.id}, {self.tipo}'

    #quando si vuole modificare un attributo di istanza
    @property
    def noleggio(self):
        return self._noleggio

    @noleggio.setter
    def noleggio(self, value):
        if not isinstance(value, bool):
            raise ValueError("noleggio deve essere booleano")
        self._noleggio = value

    def imposta_km(self, valore):
        self.km = valore


@dataclass
class SubCategory(Category):
    extra: str = None #5

    def __str__(self):
        return f'{self.category_name}, {self.id},{self.tipo}, {self.extra}'


#NB:
# noleggio e km essendo impostati di default, non li inizializzo subito
# inoltre, per creare la subCategory basta specificare in più gli attributi propri della sotto classe
if __name__ == '__main__':
    cat = Category(2, 'Cabrio')
    cat.noleggio = True
    cat.imposta_km(1000)

    sub = SubCategory(1, 'Stelvio', extra='500%%')

    print(cat)
    print(sub)





