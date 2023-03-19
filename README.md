# Python basics

Questo repository viene utilizzato per imparare e migliorare le proprie competenze su python. Seguirò diversi tutorial e approfondirò diverse librerie
che potrebbero servirmi in diverse occasioni.

Mentre si sviluppa un programma in python si può decidere di utilizzare il virtual enviroment globale del PC che si crea quando viene
installato python per la prima volta, oppure si può creare un virtual enviroment locale per il progetto. 

Il virtual enviroment locale consente di scaricare delle librerie o moduli indipendenti dagli altri progetti. Il comando per 
creare un virtual enviroment locale per il progetto è: ```python -m venv nomeEnviroment``` 

## Errori comuni

**Impossibile caricare il file activate.ps1**

Questo errore dipende dalle impostazioni di security policy attivate nel pc locale. Ecco come risolvere (indipendentemente da win10 o win11):
1. Aprire PowerShell come amministratore ed eseguire il comando ```Get-ExecutionPolicy -List```. Verrà visualizzata una tabella indicante le diverse impostazioni di sicurezza relative ai diversi scopi.
2. Eseguire il comando ```Set-ExecutionPolicy RemoteSigned``` per cambiare le impostazioni del gruppo ```LocalMachine```
3. Per visualizzare se il comando è andato a buon fine, eseguire nuovamente il comando ```Get-ExecutionPolicy -List```.

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

La differenza tra tuple e liste consiste nel fatto che le liste contengono un insieme di dati che possono essere modificati o al quale si può 
aggiungere altri tipi di dati, mentre le tuple contengono un insieme di dati che non possono essere modificati.

Le stringhe vengono considerate come degli array, ogni lettera e ogni spazio ha un indice di riferimento. Il primo indice 
ha valore 0


## Materiale

1. [Corso Python Completo 2023](https://www.youtube.com/watch?v=n093-I6K_oQ&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF), corso per imparare le basi di python e vedere come vengono traslati i normali 
costruttori per modificare il flusso dell'algoritmo.