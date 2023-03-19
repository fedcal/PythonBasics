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


## Materiale

1. [Corso Python Completo 2023](https://www.youtube.com/watch?v=n093-I6K_oQ&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF), corso per imparare le basi di python e vedere come vengono traslati i normali 
costruttori per modificare il flusso dell'algoritmo.