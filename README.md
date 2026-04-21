# Lazio Performance Analysis ⚽📊

![Tabella confronto](images/tabella_confronto.png)

Confronto delle prestazioni della **Lazio tra le stagioni di Serie A 2019/2020 e 2024/2025** utilizzando metriche di football analytics.

---

# Obiettivo del progetto

Questo progetto analizza e confronta le prestazioni della **Lazio in due stagioni di Serie A**:

- **2019/2020**
- **2024/2025**

L'analisi considera **le prime 19 giornate di campionato (girone di andata)** per entrambe le stagioni.

L’obiettivo è valutare le differenze di performance attraverso **statistiche calcistiche e metriche avanzate utilizzate nella football analytics**.

# Perché queste due stagioni?

La scelta è caduta su queste due stagioni perché, osservando le partite del girone di andata, le due Lazio sembravano simili nel rendimento complessivo — nonostante le rose fossero molto diverse per qualità e profilo dei giocatori.

L'analisi nasce proprio da questa domanda: **i numeri confermano o smentiscono questa percezione?**

I dati mostrano che l'intuizione era corretta: le due stagioni sono sorprendentemente simili in molte metriche chiave, pur con differenze significative in fase difensiva.

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
│   ├── data
│   │   ├── lazio_2019_2020_andata.csv
│   │   ├── lazio_2024_2025_andata.csv
│   │   └── lazio_dataset_completo.csv
│   ├── images
│   │   ├── conversione_tiri.png
│   │   ├── dataiku_dashboard.png
│   │   ├── dataiku_grafici.png
│   │   ├── efficienza_offensiva_media.png
│   │   ├── media_gol_fatti.png
│   │   ├── media_gol_subiti.png
│   │   ├── metabase_dashboard.png
│   │   ├── precisione_tiri.png
│   │   ├── tabella_confronto.png
│   │   └── xg_medio.png
│   ├── notebooks
│   │   ├── grafici_dataset_unito.ipynb
│   │   └── grafici.ipynb
│   ├── pipeline
│   │   ├── crea_dataset.py
│   │   └── data_pipeline.py
│   ├── README.md
│   └── requirements.txt

---

# Visualizzazioni

![Media gol fatti](images/media_gol_fatti.png)

![Media gol subiti](images/media_gol_subiti.png)

![xG medio](images/xg_medio.png)

![Efficienza offensiva](images/efficienza_offensiva_media.png)

![Precisione tiri](images/precisione_tiri.png)

![Conversione tiri](images/conversione_tiri.png)

# Risultati

Confronto delle metriche chiave nelle prime 19 giornate (girone di andata):

| Metrica                  | 2019/2020 | 2024/2025 | Differenza        |
|--------------------------|-----------|-----------|-------------------|
| Media gol fatti          | 2.18      | 1.74      | -0.44 ↓           |
| Media gol subiti         | 0.89      | 1.42      | +0.53 ↑           |
| xG medio                 | 1.86      | 1.84      | -0.02 (~uguale)   |
| Efficienza offensiva     | 1.14      | 1.01      | -0.13 ↓           |
| Precisione tiri          | 0.40      | 0.405     | +0.005 (~uguale)  |
| Conversione tiri         | 0.130     | 0.128     | -0.002 (~uguale)  |

# Insight principali

### 1. Le due squadre creano occasioni in modo quasi identico
L'xG medio è praticamente uguale (1.86 vs 1.84): entrambe le Lazio hanno prodotto la stessa qualità di occasioni da gol per partita. Nonostante rose diverse, il sistema di gioco ha portato allo stesso volume di pericolo offensivo.

### 2. La differenza vera è nella fase difensiva
La Lazio 2019/2020 subiva in media 0.89 gol a partita; la 2024/2025 ne subisce 1.42. È l'unico dato con uno scarto significativo (+59%), e spiega perché la prima stagione viene ricordata come più solida.

### 3. La Lazio 2019/2020 sfruttava meglio le occasioni
L'efficienza offensiva (gol/xG) era 1.14 contro 1.01: la squadra di Inzaghi segnava più di quanto le occasioni create facessero prevedere, un segnale di grande concretezza sotto porta.

### 4. I numeri confermano la percezione
I dati validano l'ipotesi di partenza: le due Lazio si assomigliano molto in fase offensiva, ma si distanziano chiaramente in difesa.

---

# Pipeline Dataiku

Parte del progetto è stata replicata anche utilizzando **Dataiku**, per dimostrare una **pipeline di trasformazione dati visuale**.

Struttura della pipeline:

Dataset → Prepare → Group → Dashboard

La pipeline Dataiku esegue:

- preparazione dei dati
- calcolo delle metriche di football analytics
- aggregazione per stagione
- creazione di grafici di confronto

![Dashboard Dataiku](images/dataiku_dashboard.png)

---

# Dashboard Metabase

Il dataset finale è stato collegato anche a **Metabase** per creare una dashboard di Business Intelligence.

In Metabase sono state create visualizzazioni che confrontano le due stagioni attraverso:

- media gol fatti
- media gol subiti
- xG medio
- efficienza offensiva
- precisione tiri
- conversione tiri

Le metriche sono state calcolate tramite **colonne calcolate direttamente nella piattaforma** e aggregate per stagione.

Questo permette di visualizzare rapidamente le differenze di performance tra le due stagioni.

![Dashboard Metabase](images/metabase_dashboard.png)

---

# Tecnologie utilizzate

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook  
- Dataiku  
- Metabase  

---

# Conclusione

Questo progetto mostra un flusso completo di **data analysis applicato al calcio**.

Il lavoro include:

- raccolta e preparazione dei dati
- sviluppo di una pipeline dati in Python
- creazione di metriche di football analytics
- visualizzazione dei dati tramite grafici
- costruzione di pipeline visuali con Dataiku
- creazione di dashboard interattive con Metabase

L'obiettivo è dimostrare come strumenti diversi possano essere integrati in un unico progetto di **analisi dati sportiva**, passando dalla preparazione dei dati fino alla visualizzazione finale delle informazioni.