import pandas as pd

df = pd.DataFrame(columns=['A'])

print(df)

for i in range(5):
    df = pd.concat([df, pd.DataFrame([{'A':i}])], ignore_index=True)

print(df)
