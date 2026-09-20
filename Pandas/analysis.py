import pandas as pd 
df = pd.read_csv("Data\sales.csv")
print(df)

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order_Date into date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n--- After Cleaning ---")
print("Total rows:", len(df))
print(df.head())

df["Revenue"] = df["Quantity"] * df["Price"]

print("\n--- Revenue Added ---")
print(df[["Product", "Quantity", "Price", "Revenue"]])

print("\n--- Product-wise Revenue ---")

product_sales = df.groupby("Product")["Revenue"].sum()

print(product_sales)

print("\n--- City-wise Revenue ---")

city_sales = df.groupby("City")["Revenue"].sum()

print(city_sales)

print("\n--- Total Revenue ---")

total_revenue = df["Revenue"].sum()

print("Total Revenue: ₹", total_revenue)

print("\n--- Best Selling Product ---")

best_product = df.groupby("Product")["Quantity"].sum().idxmax()

print("Best Selling Product:", best_product)

