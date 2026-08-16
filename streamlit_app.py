import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

# Load Dataset
df = pd.read_csv("superstore.csv")

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.replace("-", "_", regex=False)
      .str.replace(" ", "_", regex=False)
)

#  Uncomment this line to debug column names if issues persist:
st.write(df.columns.tolist())

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

st.title("Global Superstore Dashboard")

#  Detect Sub_Category column name dynamically
sub_cat_col = next(
    (c for c in df.columns if "sub" in c.lower() and "cat" in c.lower()), 
    None
)

st.sidebar.header("Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

#  Only show Sub-Category filter if column exists
if sub_cat_col:
    sub_category = st.sidebar.multiselect(
        "Select Sub-Category",
        options=df[sub_cat_col].unique(),
        default=df[sub_cat_col].unique()
    )
else:
    st.sidebar.warning("Sub-Category column not found in data.")
    sub_category = None

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

if sub_cat_col and sub_category is not None:
    filtered_df = filtered_df[filtered_df[sub_cat_col].isin(sub_category)]

# KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

# Charts
sales_chart = px.bar(
    filtered_df.groupby("Region")["Sales"].sum().reset_index(),
    x="Region", y="Sales", title="Total Sales by Region", color="Region"
)
st.plotly_chart(sales_chart, use_container_width=True)

profit_chart = px.bar(
    filtered_df.groupby("Category")["Profit"].sum().reset_index(),
    x="Category", y="Profit", title="Profit by Category", color="Category"
)
st.plotly_chart(profit_chart, use_container_width=True)

#  Handle both possible customer column names
customer_col = "Customer.Name" if "Customer.Name" in df.columns else "Customer Name"
top_customers = (
    filtered_df.groupby(customer_col)["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_customer_chart = px.bar(
    top_customers,
    x=customer_col, y="Sales", title="Top 5 Customers by Sales", color="Sales"
)
st.plotly_chart(top_customer_chart, use_container_width=True)

st.subheader("Filtered Dataset")
st.dataframe(filtered_df)