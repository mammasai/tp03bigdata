import pandas as pd
import sys

# ضبط الترميز لتفادي أخطاء الأحرف في الـ Terminal
sys.stdout.reconfigure(encoding='utf-8')

# قراءة البيانات من المسار المحدد
df = pd.read_csv("data/Sample - Superstore.csv", encoding="cp1252")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")

print("--- Profit by Category ---")
print(df.groupby("Category")["Profit"].sum().round(2))

print("\n--- Profit by Sub-Category (Lowest First) ---")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values().round(2).head(5))

print("\n--- Sales by Month (Total) ---")
print(df.groupby(df["Order Date"].dt.month)["Sales"].sum().round(2))

print("\n--- Sales by Segment ---")
print(df.groupby("Segment")["Sales"].sum().round(2))