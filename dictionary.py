def main():
    persona = {
        "nome":"Federico",
        "cognome":"Calò",
        "età":25
    }

    # Vi sono diversi modi per poter accedere agli elementi di un insieme
    print(persona["nome"])
    print(persona.get("nome"))
    print(persona.keys()) # lista di key
    print(persona.values())
    print(persona.items()) # lista di tuple

    # Verificare se esiste una chiave
    print("nome" in persona)

    # Modificare dei valori all'interno del dictionary
    # Questi metodi servono anche ad aggiungere una chiave inesistente
    persona["nome"] = "Marco"
    persona.update({"nome":"Anna"})

    # Per rimuovere vi sono diversi metodi: il primo per eliminare uno specifico elemento
    # il secondo per eliminare l'ultimo elemento
    # il terzo per pulire il dictionary
    # il quarto per eliminarlo completamente
    persona.pop("nome")
    persona.popitem()
    persona.clear()
    del persona

    # Per ciclare sugli elementi del dizionario bisogna fare come le liste, ma facendo riferimento alle chiavi
    for x in persona:
        print(persona[x])
    # Oppure
    for x in persona.values():
        print(x)