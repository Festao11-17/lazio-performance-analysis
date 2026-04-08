# Lazio Performance Analysis ⚽📊

![Efficienza offensiva](images/efficienza_offensiva_media.png)

Confronto delle prestazioni della **Lazio tra le stagioni di Serie A 2019/2020 e 2024/2025** utilizzando metriche di football analytics.

---

# Obiettivo del progetto

Questo progetto analizza e confronta le prestazioni della **Lazio in due stagioni di Serie A**:

- **2019/2020**
- **2024/2025**

L'analisi considera **le prime 19 giornate di campionato (girone di andata)** per entrambe le stagioni.

L’obiettivo è valutare le differenze di performance attraverso **statistiche calcistiche e metriche avanzate utilizzate nella football analytics**.

---

# Dataset

I dati sono stati raccolti manualmente partita per partita e organizzati in file **CSV**.

Per ogni partita sono state registrate le seguenti informazioni.

## Informazioni partita

- giornata  
- avversario  
- casa / trasferta  

## Performance della squadra

- gol fatti  
- gol subiti  
- tiri  
- tiri in porta  
- possesso palla  
- expected goals (**xG**)

## Distribuzione dei gol

- gol fatti 1° tempo  
- gol fatti 2° tempo  
- gol subiti 1° tempo  
- gol subiti 2° tempo  
- gol nei minuti di recupero  

Dataset finale generato:

data/lazio_dataset_completo.csv

---

# Metriche analizzate

Oltre alle statistiche base sono state calcolate alcune **metriche avanzate utilizzate nell’analisi calcistica**.

## Efficienza offensiva

Misura quanto una squadra segna rispetto alla qualità delle occasioni create.

Formula:

efficienza_offensiva = gol_fatti / xG

---

## Precisione tiri

Indica la percentuale di tiri che finiscono nello specchio della porta.

Formula:

precisione_tiri = tiri_in_porta / tiri

---

## Conversione tiri

Indica quanti tiri vengono trasformati in gol.

Formula:

conversione_tiri = gol_fatti / tiri

---

## Overperformance xG

Valuta se una squadra segna **più o meno rispetto a quanto previsto dal modello xG**.

Formula:

overperformance_xg = gol_fatti - xG

---

# Pipeline dati

Il progetto include una **pipeline di trasformazione dati sviluppata in Python**.

Fasi della pipeline:

1. Caricamento dataset stagioni  
2. Pulizia e verifica dei dati  
3. Calcolo delle metriche avanzate  
4. Unione dei dataset  
5. Creazione del dataset finale  

Script principale:

pipeline/data_pipeline.py

---

# Struttura del progetto

lazio-analysis
│
├── data
│ ├── lazio_2019_2020_andata.csv
│ ├── lazio_2024_2025_andata.csv
│ └── lazio_dataset_completo.csv
│
├── images
│ ├── conversione_tiri.png
│ ├── dataiku_dashboard.png
│ ├── dataiku_grafci.png
│ ├── efficienza_offensiva_media.png
│ ├── media_gol_fatti.png
│ ├── media_gol_subiti.png
│ ├── precisione_tiri.png
│ ├── tabella_confronto.png
│ └── xg_medio.png
│
├── notebooks
│ ├── grafici_dataset_unito.ipynb
│ └── grafici.ipynb
│
├── pipeline
│ ├── crea_dataset.py
│ └── data_pipeline.py
│
├── README.md
└── requirements.txt

![Dashboard](images/dataiku_dashboard.png)

![Grafici](images/dataiku_grafici.png.png)

![Confronto tabelle](images/tabella_confronto.png)

# Tecnologie utilizzate

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook  
- Dataiku  

---

# Possibili sviluppi futuri

Il progetto sarà esteso concludendo con:

- dashboard interattive con **Metabase**