def main():
    # Definizione di una lista. Possono contenere sia elementi di un solo tipo o elementi di diverso tipo.
    # Le liste sono identificate dalle PARENTESI QUADRE
    x = ["Milano","Roma","Napoli"]
    y = ["Ciao", 5, True]
    print(len(x))

    # Costruttore generale di una lista
    z = list(("Soleto","Lecce","Gallipoli"))

    # Accesso agli elemmenti di una lista
    # Si possono utilizzare i range utilizzati nelle stringhe per accedere agli elemmenti della lista
    print(x[2])

    # Modificare gli elemmenti di una lista
    y[2] = "Pluto"

    # Inserire un nuovo elemento
    x.append("Treviso")
    x.insert(1,"brescia")       # In questo caso possiamo scegliere anche la posizione in cui inserire l'elemento

    # Concatenazione di due liste
    x.extend(y)

    # Vi sono diversi metodi per rimuovere degli elementi
    # Rimuove solo l'elemento specificato
    x.remove("Roma")
    # Può rimuovere l'ultimo elememnto se non specifichiamo nessun indice, specificando un indice rimuove quell'elemento particolare
    x.pop()
    # Stesso significato di pop, se non viene passato nessun indice elimina tutta la lista
    del x[0]
    # Per pulire la lista
    x.clear()

    # Ciclare sugli elementi
    for citta in x:
        print(citta)

    for i in range(len(x)):
        print(x[i])

    # List commpression -> [espressione for item in lista if condizione == True]
    [print(citta) for citta in x if citta=="Roma"]

    # Ordinamento lista

    x.sort()
    x.sort(reverse=True) # Vi sono anche le Sort Compresion

    # In questo mod creaiamo un riferimento alla lista x
    pippo = x

    # Se dovessimo copiare la lista x in un'altra lista ci basterebbe fare:
    pluto = x.copy()