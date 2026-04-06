import pandas as pd

lazio_2019 = pd.read_csv("data/lazio_2019_2020_andata.csv")
lazio_2024 = pd.read_csv("data/lazio_2024_2025_andata.csv")

lazio_2019["stagione"] = "2019_2020"
lazio_2024["stagione"] = "2024_2025"

lazio = pd.concat([lazio_2019, lazio_2024])

print(lazio.head())

print(len(lazio))

print(lazio["stagione"].value_counts())

lazio.to_csv("data/lazio_dataset_completo.csv", index=False)