if __name__ == '__main__':

    # Utilizzo zip per creare una lista
    L1 = [1,2,3,4]
    L2 = [5,6,7,8]
    print(list(zip(L1,L2)))

    # Creiamo un dizionario
    keys = ['nome','cognome','età']
    values = ['Federico','Calò',25]

    dict = {}
    for (k,v) in zip(keys,values):
        dict[k] = v