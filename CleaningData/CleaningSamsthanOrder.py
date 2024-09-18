import pandas as pd

columnIndex = 0
isDropBillingName = False
rows_to_drop = []

df = pd.read_csv(r"/Users/ansh/Downloads/samsthanorderlist.csv")

#Dropping uneeded columns
df = df.drop(columns=["status", "created_on", "fulfilled_on", "disputed_on", "refunded_on", "shipping_total", "discounts_code"])
df = df.drop(columns=df.columns[4:21])
df = df.drop(columns=df.columns[9:19])
df = df.drop(columns=df.columns[10:21])
df = df.drop(columns=["discounts_total", "taxes_total", 'order_total'])


for x in df.index:
    #Removing orders that are actually donations
    if df.loc[x, "items_count"] > 50 or df.loc[x, "line_item_product"] == "General Donation":
        rows_to_drop.append(x)

    if df.loc[x, "line_item_product"] == 'Test':
        rows_to_drop.append(x)



    #Removing the billing_name if the name matches
    if df.loc[x, "customer_full_name"] == df.loc[x, "billing_address_addressee"]:
        isDropBillingName = True
    else:
        isDropBillingName = False

    #Converts all fullnames into the correct format
    df.loc[x, "customer_full_name"] = df.loc[x, "customer_full_name"].replace(df.loc[x, "customer_full_name"], df.loc[x, "customer_full_name"].title())

df.drop(index=rows_to_drop, inplace=True)

if isDropBillingName:
    df.drop(columns=["billing_address_addressee"], inplace=True)

df['items_count'] = df['items_count'].astype(str)

df = df.sort_values(by='customer_full_name')


# Trying to combine subtotal and add it
df["subtotal"] = df["subtotal"].str.replace("$", "")
df["subtotal"] = df["subtotal"].str.replace(".00", "")

df['subtotal'] = df['subtotal'].astype(int)

df = df.groupby(['customer_full_name', 'customer_email']).agg({'line_item_product': ', '.join, 'items_count' : lambda x: ', '.join(map(str, x)), 'subtotal' : 'sum'}).reset_index()


df.reset_index(drop=True, inplace=True)



df.to_csv("/Users/ansh/Downloads/exportorder2.csv")
