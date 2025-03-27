import pandas as pd

columnIndex = 0
isDropBillingName = False
rows_to_drop = []

# Load the dataset
df = pd.read_csv(r"/Users/ansh/Downloads/decemberorders.csv")

# Dropping unnecessary columns
df = df.drop(columns=["status", "created_on", "fulfilled_on", "disputed_on", "refunded_on", "shipping_total", "discounts_code"])
df = df.drop(columns=df.columns[4:21])
df = df.drop(columns=df.columns[9:19])
df = df.drop(columns=df.columns[10:21])
df = df.drop(columns=["discounts_total", "taxes_total", "order_total", "subtotal"])  # Dropping 'subtotal'

# Process rows
for x in df.index:
    # Removing orders that are actually donations
    if df.loc[x, "items_count"] > 50 or df.loc[x, "line_item_product"] == "General Donation":
        rows_to_drop.append(x)

    if df.loc[x, "line_item_product"] == 'Test':
        rows_to_drop.append(x)

    # Removing the billing_name if the name matches
    if df.loc[x, "customer_full_name"] == df.loc[x, "billing_address_addressee"]:
        isDropBillingName = True
    else:
        isDropBillingName = False

    # Converts all full names into the correct format
    df.loc[x, "customer_full_name"] = df.loc[x, "customer_full_name"].title()

# Drop identified rows
df.drop(index=rows_to_drop, inplace=True)

# Drop the 'billing_address_addressee' column if required
if isDropBillingName:
    df.drop(columns=["billing_address_addressee"], inplace=True)

# Ensure 'items_count' is a string
df['items_count'] = df['items_count'].astype(str)

# Sort data by customer name
df = df.sort_values(by='customer_full_name')

# Save the cleaned data
df.to_csv("/Users/ansh/Downloads/decemberorderlist.csv", index=False)
