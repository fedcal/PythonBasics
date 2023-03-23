# Python basics


## Intro

Questo repository viene utilizzato per imparare e migliorare le proprie competenze su python. Seguirò diversi tutorial e approfondirò diverse librerie
che potrebbero servirmi in diverse occasioni.

Mentre si sviluppa un programma in python si può decidere di utilizzare il virtual enviroment globale del PC che si crea quando viene
installato python per la prima volta, oppure si può creare un virtual enviroment locale per il progetto. 

Il virtual enviroment locale consente di scaricare delle librerie o moduli indipendenti dagli altri progetti. Il comando per 
creare un virtual enviroment locale per il progetto è: ```python -m venv nomeEnviroment``` 

In python le variabili devono essere valorizzate nel momento in cui vengono dichiarate o nel momento in cui si ha bisogno. Una variabile 
può contenere diversi **tipi** di oggetti. Come in tutti i linguaggi, si attribuisce un nome alle variabili che identificano il significato della 
variabile. Possono essere utilizzati diversi case, anche tutto in maiuscolo. E' vietato inserire un numero a inizio variabile, oppure utilizzare un trattino.

Vi sono diversi tipi di dati che possiamo gestire in python, inoltre una stessa variabile può contenere diversi tipologie di dati durante l'esecuzione 
del programma. I principali tipi di dati semplici sono:

- Stringhe: "ciao"
- Interi: 5
- float: 5.5
- booleani: True/False

Ci sono anche altri tipi di dati più complessi che prendono il nome di collezioni:

- Liste: ["roma","milano"]
- tuple: ("roma","milano")
- range: range(6)
- dizionario: {"nome":"Federico", "eta":25}
- insiemi: {"roma","Lecce"}

Le proprietà basilari di una collezione sono:
1. _ordinamento_: la collezione contiene eleemmmnti che seguono un determinato ordine e l'aggiunta di un nuovo elemento non incide su questo
2. _indicizzazione_: possiamo accedere agli elementi di una collezione tramite un indice
3. _modificabile_: possiamo aggiungere, cambiare e rimuovere gli elementi della collezione
4. _immutabile_: non possiamo aggiungere, cambiare e rimuovere gli elementi
5. _elementi duplicati_: possiamo inserire all'interno della collezione più elementi con lo stesso valore

La differenza tra tuple e liste consiste nel fatto che le liste contengono un insieme di dati che possono essere modificati o al quale si può 
aggiungere altri tipi di dati, mentre le tuple contengono un insieme di dati che non possono essere modificati. Entrambe queste collezioni sono ordinate.

Gli insiemi richiamano il relativo concetto matematico, non sono ordinati e non hanno un indice. I dizionari corrispondono ai map in Java,
ovvero una particolare struttura di dati chiave valore.
Gli insiemi non hanno un ordinamento, non sono indicizzati, ma le chiavi rappresentano una 
sorta di chiave di accesso. Questo fa si che gli insiemi non sono modificabili. Gli insiemi e i dizionari non permettono duplicati.

Le stringhe vengono considerate come degli array, ogni lettera e ogni spazio ha un indice di riferimento. Il primo indice 
ha valore 0.

Analizziamo _l'istruzione di assegnamento_ tramite la quale si assegna un valore a una variabile. In python l'assegnamento 
crea referenze a degli oggetti e non una loro copia, questo porta a trattare le variabili come dei puntatori. Inoltre, 
i nomi vengono creati la prima volta che vengono assegnati e una volta fatto ciò, il valore delle variabili viene rimpiazzato 
nel corso dell'esecuzione del programma. Python non permette di referenziare nomi se prima non vengono assegnati.

**Varie forme di assegnazione**

|              Forma di assegnazione              |              Significato               |
|:-----------------------------------------------:|:--------------------------------------:|
|            ```prova1 = 'Federico'```            |     Forma semplice di assegnazione     |
|    ```prova1, prova2 = 'Federico', 'Calò'```    |  Assegnazione di tupla (posizionale)   |
| ```[prova1, prova2] = ['valore1', 'Valore2']``` |  Assegnazione di tupla (posizionale)   |
|           ```a, b, c, d = 'prova'```            | Assegnamento sequenziale generalizzato |
|         ```var1 = var2 = 'variabile'```         |         Assegnamento multiplos         |
|                ```indice += 1```                |          Assegnamento esteso           |

**Alcune parole chiavi dei cili**

Le parole chiavi per definire un ciclo sono costituite da ```while```,```do - while``` e ```for```. Ci sono alcune parole 
che modificano la normale esecuzione del ciclo:

- ```break```: esce dal ciclo e riprende il normale flusso del programma dall'istruzione successiva ad esso
- ```continue```: salta alla prossima iterazione del ciclo
- ```pass```: non fa nulla. Viene utilizzata quando non abbiamo nulla di significativo da fare, ma vi è una funzione che richiede qualcosa

Vi sono due modi particolari per ciclare utilizzando le funzioni ```range``` e ```zip```. Range viene utilizzato per creare 
dei range di numeri del tipo: range(3) genererà una lista di numeri 1,2,3, oppure intervalli del tipo: range(-2,2) genererà 
un intervallo di numeri da -2, -1, 0, 1, 2. Questa funzione permette di ciclare in particolari circostanze, ad esempio se 
dovessimo prendere le posizioni di una lista ogni 2. Per fare ciò basta utilizzare la funzione range in questo modo: 
```range(start,stop,step)```, ovvero indicando con start il valore di inizio, con stop il valore di fine e con step il salto 
tra un valore e l'altro che il contatore deve fare.

Con il comando zip possiamo creare delle liste di tuple partendo da due liste. Un esempio lo trovate [in questo file](prove.py), 
nel quale creiamo anche dei dizionari sfruttando los tesso comando.


### Lavorare con i file
Vi sono diversi tipi per memorizzare le informazioni. In base a ciò che serve vengono utilizzati i file o un database. 
Inziamo ad analizzare i file e vediamo come scriverci dentro.

Prima di analizzare le funzioni per la creazione, lettura, scrittura e modifica di un file di testo, vediamo i diversi modi
di aprire un file:

| Simbolo |              Significato               |
|:-------:|:--------------------------------------:|
|    w    |      Aprire un file in scrittura       |
|    r    |       Aprire un file in lettura        |
|    x    |           Creazione del file           |
|    a    | Aprire un file per aggiungere qualcosa |

Inoltre si può decidere se aprire il file in modalità binaria, con il simbolo ```b```, o in modalità testuale, con il 
simbolo ```t```. Quindi potremmo avere delle combinazioni del tipo ```wb``` per aprire un file binario e scriverci dentro 
qualcosa.

Per aprire un file si utilizza il metodo open() in questo modo: ```nome variabile = open("percorso_file", "modalità_di_aperutra")```.
Ci sono diversi modi per leggere il contenuto di un file, considerando che python lo considera come stringa, conviene 
leggere riga per riga. Dopo l'apertura del file vi è il metodo close() che permette l'interruzione del flusso dati, anche se 
python chiude automaticamente la connessione prima del termine del programma. Inoltre python bufferizza e indicizza la lettura 
dei file, permettendo con il metodo seek di modificare particolari punti del file.

Da notare come i **file di testo** rappresentano il proprio contenuto tramite normali oggetti str, mediante i quali effettuano 
la codifica/decodifica Unicode e convertono di default i caratteri di fine riga. Mentre i **file binari** rappresentano il 
proprio contenuto tramite stringhe di tipo bytes che non modificano in alcun modo ciò che viene letto o scritto.

Una differenza tra i file di testo e i file binari consiste nel fatto che i primi, a differenza dei secondi, codificano le 
informazioni di fine riga.

## Le funzioni

Le funzioni raggruppano una serie di istruzioni volte a raggiungere un determinato scopo. Servono per riutilizzare il codice 
scritto, riducendo di fatto la ridondanza, e garantendo la decomposizone funzionale. Per definire una funzione deve essere 
utilizzato il nome def seguito dal nome della funzione e dagli eventuali argomenit. Ci sono anche funzioni un po' più 
particolari come le funzioni lambda che creano e restituiscono un oggetto. Il termine ```yeld``` invia un oggetto al 
chiamante e ne ricorda lo stato. I parametri delle funzioni vengono passati come riferimento e non vanno dichiarati, come 
anche le variabili e i valori restituiti. 

Quando scriviamo un programma in python, viene creato automaticamente uno _spazio dei nomi_, ovvero quel luogo entro cui 
il nome esiste. In generale, le variabili dichiarate all'interno di una funzione sono associate a quello specifico spazio 
dei nomi. Quindi i nomi definiti all'interno di un def potranno essere visti all'interno di quello spazio di definizione e 
non potranno mai entrare in conflitto con nomi di variabili definite all'esterno.

Se una variabile viene assegnata all'interno di una def, allora è una variabile _locale_ di quella funzione, mentre se viene 
assegnata all'interno di una def che ne racchiuda un'altra, diventa una variabile _nonlocal_. Infine se una variabile viene 

## I moduli
In Python un concetto fondamentale è rappresentato dal modulo, diverso da quello di package. Ogni file è 
un modulo e ogni modulo importa altri moduli per utilizzare i nomi in essi definiti. Con il termine ```import``` si importa 
il copdice relativo ad un modulo, mentre con la sintassi ```from x import y``` si decide di importare una specifica funzione 
da un determinato modulo.

Importando un modulo, si importano di conseguenza tutto lo spazio globale, il quale viene associato all'oggetto del modulo importato. 
L'operazione di importazione di un modulo si divide in tre fasi:
- ricerca del modulo
- compilazione del modulo
- esecuzione del modulo.

Python ha di default impostato la cartella principale dove risiede il main come cartella in cui cercare i moduli. Se 
dovessimo aggiungere altre cartelle in cui cercare, possiamo definire la variabile ```PYTHONPATH```. Questa variabile va 
modificata dal sistema operativo


## Curiosità di python
Python è un linguaggio dotato di un interprete, il cui compito consiste di interpretare a run time ogni singola linea del 
codice nel relativo linguaggio macchina.

A differenza degli altri linguaggi, Python non utilizza il punto e virgola per segnalare la fine di un'istruzione. L'interprete 
identifica il fine riga con la fine dell'istruzione. Però il punto e virgola viene utilizzato quando ci sono più istruzioni 
su una stessa riga.

## Errori comuni

**Impossibile caricare il file activate.ps1**

Questo errore dipende dalle impostazioni di security policy attivate nel pc locale. Ecco come risolvere (indipendentemente da win10 o win11):
1. Aprire PowerShell come amministratore ed eseguire il comando ```Get-ExecutionPolicy -List```. Verrà visualizzata una tabella indicante le diverse impostazioni di sicurezza relative ai diversi scopi.
2. Eseguire il comando ```Set-ExecutionPolicy RemoteSigned``` per cambiare le impostazioni del gruppo ```LocalMachine```
3. Per visualizzare se il comando è andato a buon fine, eseguire nuovamente il comando ```Get-ExecutionPolicy -List```.





## Materiale

1. [Corso Python Completo 2023](https://www.youtube.com/watch?v=n093-I6K_oQ&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF), corso per imparare le basi di python e vedere come vengono traslati i normali 
costruttori per modificare il flusso dell'algoritmo.
2. [Imparare Python](https://amzn.to/3Ty9nY6), libro molto utile per una rapida consultazione, contenente anche un po' di 
teoria relativa alla programmazione orientata agli oggetti.