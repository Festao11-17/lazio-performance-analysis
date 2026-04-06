# Lazio Performance Analysis ⚽📊

![Efficienza offensiva](images/efficienza_offensiva_media.png)

Comparison of Lazio performance between the **2019/2020** and **2024/2025** Serie A seasons using football analytics metrics.

---

# Obiettivo del progetto

Questo progetto analizza e confronta le prestazioni della **Lazio in due stagioni di Serie A**:

- **2019/2020**
- **2024/2025**

L'analisi considera **le prime 19 giornate di campionato (girone di andata)** per entrambe le stagioni.

L’obiettivo è valutare le differenze di performance attraverso **metriche statistiche e metriche avanzate utilizzate nella football analytics**.

---

# Dataset

I dati sono stati raccolti manualmente partita per partita e organizzati in file CSV.

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

Misura l'efficienza della squadra nel trasformare i tiri in gol.

Formula:

efficienza_offensiva = gol_fatti / tiri

---

## Precisione tiri

Misura la percentuale di tiri che finiscono nello specchio della porta.

Formula:

precisione_tiri = tiri_in_porta / tiri

---

## Conversione tiri

Indica la percentuale di tiri che vengono trasformati in gol.

Formula:

conversione_tiri = gol_fatti / tiri

---

## Overperformance xG

Valuta se la squadra segna più o meno rispetto a quanto previsto dal modello Expected Goals.

Formula:

overperformance_xg = gol_fatti - xG

---

# Pipeline dati

Il progetto include una **pipeline di trasformazione dati sviluppata in Python**.

Processo:

1. Caricamento dataset stagioni  
2. Pulizia e verifica dati  
3. Calcolo metriche avanzate  
4. Unione dataset  
5. Creazione dataset finale  

Script principale:

pipeline/data_pipeline.py

---

# Struttura del progetto

lazio-analysis
    ├── data
    │   ├── lazio_2019_2020_andata.csv
    │   ├── lazio_2024_2025_andata.csv
    │   └── lazio_dataset_completo.csv
    ├── images
    │   ├── conversione_tiri.png
    │   ├── efficienza_offensiva_media.png
    │   ├── media_gol_fatti.png
    │   ├── media_gol_subiti.png
    │   ├── precisione_tiri.png
    │   ├── tabella_confronto.png
    │   └── xg_medio.png
    ├── notebooks
    │   ├── grafici_dataset_unito.ipynb
    │   └── grafici.ipynb
    ├── pipeline
    │   ├── crea_dataset.py
    │   └── data_pipeline.py
    ├── README.md
    └── requirements.txt

![Tabella confronto](images/tabella_confronto.png)

---

## Visualizzazioni

![Media gol fatti](images/media_gol_fatti.png)

![Media gol subiti](images/media_gol_subiti.png)

![xG medio](images/xg_medio.png)

![Efficienza offensiva](images/efficienza_offensiva_media.png)

![Precisione tiri](images/precisione_tiri.png)

![Conversione tiri](images/conversione_tiri.png)

![Tabella confronto](images/tabella_confronto.png)

---

# Tecnologie utilizzate

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook  

---

# Possibili sviluppi futuri

Il progetto sarà essere esteso con:

- dashboard interattive con **Metabase**
- pipeline dati automatizzate con **Dataiku**