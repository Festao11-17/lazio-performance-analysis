Lazio Performance Analysis ⚽📊
Obiettivo del progetto

Questo progetto analizza e confronta le prestazioni della Lazio in due stagioni di Serie A:

    2019/2020
    2024/2025

L'analisi considera le prime 19 giornate di campionato (girone di andata) per entrambe le stagioni.

L’obiettivo è valutare le differenze di performance attraverso metriche statistiche e metriche avanzate utilizzate nella football analytics.
Dataset

I dati sono stati raccolti manualmente partita per partita e organizzati in dataset CSV.

Per ogni partita sono state registrate le seguenti informazioni:
Informazioni partita

    giornata
    avversario
    casa / trasferta

Performance della squadra

    gol fatti
    gol subiti
    tiri
    tiri in porta
    possesso palla
    expected goals (xG)

Distribuzione dei gol

    gol fatti 1° tempo
    gol fatti 2° tempo
    gol subiti 1° tempo
    gol subiti 2° tempo
    gol nei minuti di recupero

I dataset originali sono salvati nella cartella:

data/

Metriche analizzate

Oltre alle statistiche base sono state calcolate alcune metriche avanzate utilizzate nell’analisi calcistica.
Efficienza offensiva

Misura quanto una squadra segna rispetto alle occasioni create.

Efficienza offensiva = Gol fatti / xG

Conversione tiri

Indica quanti tiri vengono trasformati in gol.

Conversione tiri = Gol fatti / Tiri

Precisione tiri

Indica quanti tiri finiscono nello specchio della porta.

Precisione tiri = Tiri in porta / Tiri

Pipeline dati

Il progetto include una pipeline di trasformazione dati sviluppata in Python.

Processo:

    Caricamento dataset stagioni
    Pulizia e verifica dati
    Aggiunta variabile stagione
    Unione dataset
    Creazione dataset finale

Dataset finale generato:

data/lazio_dataset_completo.csv

Struttura del progetto

Match_Analyst
│
├── data
│   ├── lazio_2019_2020_andata.csv
│   ├── lazio_2024_2025_andata.csv
│   └── lazio_dataset_completo.csv
│
├── pipeline
│   ├── data_pipeline.py
│   ├── crea_dataset.py
│   ├── grafici.py
│   └── grafici_dataset_unito.py
│
├── notebooks
│   ├── data_pipeline.ipynb
│   ├── grafici.ipynb
│   └── grafici_dataset_unito.ipynb
│
├── immagini
│   ├── media_gol_fatti_dataset_unito.png
│   ├── media_gol_subiti_dataset_unito.png
│   ├── xG_medio_dataset_unito.png
│   ├── media_efficienza_offensiva_dataset_unito.png
│   ├── conversione_tiri.png
│   ├── precisione_tiri.png
│   └── tabella_confronto_dataset_unito.png
│
└── README.md

Visualizzazioni

Il progetto produce diversi grafici per confrontare le due stagioni.

Principali analisi visuali:

    media gol segnati per partita
    media gol subiti per partita
    xG medio
    efficienza offensiva
    conversione tiri
    precisione tiri
    tabella riassuntiva delle statistiche

Le visualizzazioni sono salvate nella cartella:

immagini/

Tecnologie utilizzate

    Python
    Pandas
    Matplotlib
    Jupyter Notebook

Possibili sviluppi futuri

Questo progetto può essere esteso includendo:

    analisi di tutte le squadre di Serie A
    confronto tra attacco e difesa delle squadre
    dashboard interattive con Metabase
    pipeline dati automatizzate con Dataiku

Autore

Progetto di analisi dati calcistici realizzato come esercizio di football data analysis e data pipeline development