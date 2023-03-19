def main():
    x = "Ciao" #stringa monoriga
    y = """Stringa
    Multi
    riga"""

    x = 'prova'
    print(x[2])         # seconda lettera
    print(len(x))       # lunghezza della stringa

    x = 'Ciao sono Federico e sono uno sviluppatore'

    # loop per leggere ogni carattere della stringa
    for carattere in x:
        print(carattere)

    print(x[:3])        # prendere le prime tre posizioni della stringa
    print(x[2:])        # escludere le prime due posizioni
    print[x[2:8]]       # range di stringa
    print(x[-4])        # prendere la 4 posizione dalla fine

    x = x.upper()       # tutte le lettere in maiuscolo
    x = x.lower()       # tutte le lettere in minuscolo
    x = x.strip()       # toglie gli spazi

    x.replace("o","w")

    # Esempio di format
    prova = "Ciao, sono {} e mi occupo di {} e di {}"
    print(prova.format('Federico','sviluppare','Design'))

