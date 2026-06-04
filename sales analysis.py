import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("train.csv")

# Display First 5 Rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset Information
print("\nDATASET INFO")
print(df.info())

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate Records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Convert Order Date to Datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Create Month Column
df["Month"] = df["Order Date"].dt.month_name()

# ==========================
# BUSINESS METRICS
# ==========================

total_sales = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("\n===== BUSINESS METRICS =====")
print("Total Sales:", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

# ==========================
# MONTHLY SALES ANALYSIS
# ==========================

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# ==========================
# TOP 10 PRODUCTS
# ==========================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print("\n===== TOP 10 PRODUCTS =====")
print(top_products.head(10))

plt.figure(figsize=(10,5))
top_products.head(10).plot(kind="bar")
plt.title("Top 10 Best Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# ==========================
# CATEGORY ANALYSIS
# ==========================

category_sales = df.groupby("Category")["Sales"].sum()

print("\n===== CATEGORY SALES =====")
print(category_sales)

plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Sales Distribution")
plt.ylabel("")
plt.show()

# ==========================
# REGION ANALYSIS
# ==========================

region_sales = df.groupby("Region")["Sales"].sum()

print("\n===== REGION SALES =====")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# ==========================
# TOP CUSTOMERS
# ==========================

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)

print("\n===== TOP 10 CUSTOMERS =====")
print(top_customers.head(10))

plt.figure(figsize=(10,5))
top_customers.head(10).plot(kind="bar")
plt.title("Top 10 Customers")
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.show()

# ==========================
# STATE ANALYSIS
# ==========================

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)

print("\n===== TOP 10 STATES =====")
print(state_sales.head(10))

plt.figure(figsize=(10,5))
state_sales.head(10).plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.show()

# ==========================
# SAVE CLEANED DATA
# ==========================

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nProject Completed Successfully!")
print("Cleaned file saved as: cleaned_sales_data.csv")
