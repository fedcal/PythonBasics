def main():
    # Definire tupole con un solo valore
    x = ("ciao",)
    # Definire lista normalmente
    y = tuple(("ciao","buongiorno","buonanotte"))
    print(type(y))
    # L'accesso alle tuple è identico a quello delle liste
    print(y[2])

    # Per verificare se esiste un elemento il una tupla
    if "ciao" in y:
        print("ok")

    delta = list(y)
    delta[0]  = "buonpomeriggio"
    y = tuple(delta)

    # Dividere una tupla in più variabili
    (a,b,c) = y

    # Oppure
    (a,*b) = y


if __name__ == '__main__':
    main()