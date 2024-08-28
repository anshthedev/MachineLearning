import pandas as pd

columnIndex = 0

df = pd.read_csv(r"/Users/ansh/Downloads/samsthanorderlist.csv")

df = df.drop(columns=["status", "created_on", "fulfilled_on", "disputed_on", "refunded_on"])
for x in df.columns:
    if 3 < columnIndex and columnIndex < 20:
        df = df.drop(columns=[x], inplace=True)

for x in df.index:
    if df.loc[x, "items_count"] > 50:
        df.drop(x, inplace=True)

    columnIndex += 1


