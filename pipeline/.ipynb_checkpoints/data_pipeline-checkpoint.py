import pandas as pd
import numpy as np

lazio_2019 = pd.read_csv("data/lazio_2019_2020_andata.csv")
lazio_2024 = pd.read_csv("data/lazio_2024_2025_andata.csv")

#print(lazio_2019.describe())
#print(lazio_2024.describe())

#print(lazio_2019.isnull().sum())
#print(lazio_2024.isnull().sum())

#print(lazio_2019["tiri"].max())
#print(lazio_2024["tiri"].max())

#gol_fatti =
lazio_2019["gol_fatti"] == (lazio_2019["gol_fatti_1T"] + lazio_2019["gol_fatti_2T"])
#print(gol_fatti)

#gol_fatti =
lazio_2024["gol_fatti"] == (lazio_2024["gol_fatti_1T"] + lazio_2024["gol_fatti_2T"])
#print(gol_fatti)

#efficienza_offensiva =
lazio_2019["efficienza_offensiva"] = lazio_2019["gol_fatti"] / lazio_2019["tiri"]
#print(efficienza_offensiva)

#efficienza_offensiva =
lazio_2024["efficienza_offensiva"] = lazio_2024["gol_fatti"] / lazio_2024["tiri"]
#print(efficienza_offensiva)

#precisione_tiro = lazio_2019["precisione_tiro"] = lazio_2019["tiri_in_porta"] / lazio_2019["tiri"]
#print(precisione_tiro)

#precisione_tiro = lazio_2024["precisione_tiro"] = lazio_2024["tiri_in_porta"] / lazio_2024["tiri"]
#print(precisione_tiro)

#overperformance_xg = lazio_2019["overperformance_xg"] = lazio_2019["gol_fatti"] - lazio_2019["xG"]
#print(overperformance_xg)

#overperformance_xg = lazio_2024["overperformance_xg"] = lazio_2024["gol_fatti"] - lazio_2024["xG"]
#print(overperformance_xg)

'''summary = pd.DataFrame({
    "metrica": [
        "gol_medi",
        "gol_subiti_medi",
        "tiri_medi",
        "possesso_medio",
        "xG_medio",
        "efficienza_offensiva"
    ],
    "lazio_2019_20": [
        lazio_2019["gol_fatti"].mean(),
        lazio_2019["gol_subiti"].mean(),
        lazio_2019["tiri"].mean(),
        lazio_2019["possesso"].mean(),
        lazio_2019["xG"].mean(),
        lazio_2019["efficienza_offensiva"].mean()
    ],
    "lazio_2024_25": [
        lazio_2024["gol_fatti"].mean(),
        lazio_2024["gol_subiti"].mean(),
        lazio_2024["tiri"].mean(),
        lazio_2024["possesso"].mean(),
        lazio_2024["xG"].mean(),
        lazio_2024["efficienza_offensiva"].mean()
    ]
})

print(summary)'''