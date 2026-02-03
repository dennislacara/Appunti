
#gestione errore TextField, input numerico
# valore numerico | None
def controllo_TexField_numerico(value):
    valore = None
    try:
        valore = int(value)
    except Exception as e:
        print(e)
        #stampa un messaggio di allerta nell'interfaccia
        # es: self._view.show_alert('Inserire un valore numerico valido')
    return valore



#gestione errore DropDown
# key (str) | None
def controllo_DD(value):
    if not value:
        # stampa un messaggio di allerta nell'interfaccia
        # es: self._view.show_alert('Inserire un valore nel dropdown')
        return
    else:
        return value


#esempio di utilizzo
def funzione_del_controller():
    valore = controllo_TexField_numerico('self._view.txt_input.value')
    if not valore:
        return
    else:
        pass

#_____________________________________________________________________________________________________________________________________


# se ci sono piu dropdown da controllare contemporaneamente (es:3)

def controllo_DDs(value1, value2, value3):
    if not value1 or not value2 or not value3:
        # stampa un messaggio di allerta nell'interfaccia
        # es: self._view.show_alert('Inserire valori nei dropdown')
        return
    else:
        return True

#esempio di utilizzo
def funzione_del_controller2():
    bool = controllo_DDs('self._view.txt_input.value1','self._view.txt_input.value2','self._view.txt_input.value3')
    if not bool:
        return
    #...eventuale controllo di un Texfield con elif
    #e infine un else in cui si entra se ci sono tutti i dati




