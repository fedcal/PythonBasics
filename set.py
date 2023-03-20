def main():
    #Tipi di dichiarazione di un set. Non sono indicizzati e non ordinati
    y = {"Lecce","Milano","Roma"}
    x = {"Ciao",5,True}
    z = set(("Lecce","Milano","Roma"))

    # Accesso a un dizionario
    for delta in y:
        print(y)
    # Aggiungere un elemento
    y.add("Maglie")

    #Rimuovere un elemento
    y.remove("Lecce")

    # Con discard possiamo eliminare un elemento anche se l'elemento non è presente nel set
    y.remove("Galatina")

    # Eliminare un insieme
    del x

    # pulire un insieme
    x.clear()

    alpha = {"Maglie","Otranto","Gallipoli"}

    # Per fare l'unione di due insiemi -> si crea un nuovo set
    # Anche update ha la stessa funzionalità -> aggiorna il set
    # Entrambi escludono gli elementi duplicati
    gamma = x.union(y)
    x.update(y)

    # nel caso si volesse lavorare con gli elementi duplicati
    # intersection -> crea un nuovo set
    x.intersection_update(y)
    z = x.intersection(y)

    # Se si vuole escludere i duplicati
    x.symmetric_difference_update()