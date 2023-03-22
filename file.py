if __name__ == '__main__':
    firstFile = open("FirstFile.txt","wt") # La modalità scrittura crea il file se non esiste
    firstFile.write("Questo è il primo file di testo generato con python\n") # scriviamo nel file
    firstFile.close() # Chiudiamo il buffer

    firstFile = open("FirstFile.txt","rt")  # Apriamo il file in modalità lettura, anche se questa è implicita se lasciamo
                                            # il relativo campo vuoto
    print(firstFile.readline())

    # Se si necessita la lettura dell'intero file
    open('FirstFile.txt').read()
    # Mentre se siamo interessati alle singole linee
    for line in firstFile:
        print(line)

    firstFile.close()

    # Proviamo a salvare un dizionario all'interno del file
    firstFile = open("FirstFile.txt","at")  # Apriamo il file in append (quindi aggiungeremo l'oggetto in coda al testo
                                            # già presente
    persona = {
        "nome":"Federico",
        "cognome": "Calò",
        "età": 25
    }

    for x in persona:
        firstFile.write(x+":"+str(persona[x])+"\n")

    firstFile.close()