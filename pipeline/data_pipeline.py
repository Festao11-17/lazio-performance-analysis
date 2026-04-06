import pandas as pd

# ============================================================
# DATA PIPELINE - LAZIO PERFORMANCE ANALYSIS
# ============================================================
# Questo script prepara i dataset delle due stagioni e calcola
# alcune metriche avanzate di performance offensiva.
#
# Metriche calcolate:
#
# 1) Efficienza Offensiva
#    Formula:
#    efficienza_offensiva = gol_fatti / tiri
#
#    Indica quanti gol vengono segnati per ogni tiro effettuato.
#
#
# 2) Precisione Tiri
#    Formula:
#    precisione_tiri = tiri_in_porta / tiri
#
#    Misura quanto spesso i tiri finiscono nello specchio.
#
#
# 3) Conversione Tiri
#    Formula:
#    conversione_tiri = gol_fatti / tiri_in_porta
#
#    Indica quanto spesso i tiri in porta diventano gol.
#
#
# 4) Overperformance xG
#    Formula:
#    overperformance_xg = gol_fatti - xG
#
#    Valuta se la squadra segna più o meno di quanto previsto
#    dal modello Expected Goals.
# ============================================================


# ------------------------------------------------------------
# Funzione per preparare il dataset
# ------------------------------------------------------------
def prepara_dataset(df):

    # Calcolo dei gol totali
    df["gol_fatti"] = df["gol_fatti_1T"] + df["gol_fatti_2T"]

    # Efficienza offensiva
    df["efficienza_offensiva"] = df["gol_fatti"] / df["tiri"]

    # Precisione dei tiri
    df["precisione_tiri"] = df["tiri_in_porta"] / df["tiri"]

    # Conversione dei tiri in porta
    df["conversione_tiri"] = df["gol_fatti"] / df["tiri_in_porta"]

    # Differenza tra gol segnati e Expected Goals
    df["overperformance_xg"] = df["gol_fatti"] - df["xG"]

    return df


# ------------------------------------------------------------
# Caricamento dataset
# ------------------------------------------------------------
lazio_2019 = pd.read_csv("data/lazio_2019_2020_andata.csv")
lazio_2024 = pd.read_csv("data/lazio_2024_2025_andata.csv")


# ------------------------------------------------------------
# Preparazione dataset con le metriche avanzate
# ------------------------------------------------------------
lazio_2019 = prepara_dataset(lazio_2019)
lazio_2024 = prepara_dataset(lazio_2024)


# ------------------------------------------------------------
# Tabella di confronto tra le due stagioni
# ------------------------------------------------------------
summary = pd.DataFrame({
    "metrica": [
        "gol_fatti_medi",
        "gol_subiti_medi",
        "tiri_medi",
        "possesso_medio",
        "xG_medio",
        "efficienza_offensiva_media",
        "precisione_tiri_media",
        "conversione_tiri_media"
    ],

    "lazio_2019_20": [
        lazio_2019["gol_fatti"].mean(),
        lazio_2019["gol_subiti"].mean(),
        lazio_2019["tiri"].mean(),
        lazio_2019["possesso"].mean(),
        lazio_2019["xG"].mean(),
        lazio_2019["efficienza_offensiva"].mean(),
        lazio_2019["precisione_tiri"].mean(),
        lazio_2019["conversione_tiri"].mean()
    ],

    "lazio_2024_25": [
        lazio_2024["gol_fatti"].mean(),
        lazio_2024["gol_subiti"].mean(),
        lazio_2024["tiri"].mean(),
        lazio_2024["possesso"].mean(),
        lazio_2024["xG"].mean(),
        lazio_2024["efficienza_offensiva"].mean(),
        lazio_2024["precisione_tiri"].mean(),
        lazio_2024["conversione_tiri"].mean()
    ]
})


# ------------------------------------------------------------
# Output finale
# ------------------------------------------------------------
print(summary)