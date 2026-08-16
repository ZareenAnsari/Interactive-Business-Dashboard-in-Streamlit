# Interactive Business Dashboard in Streamlit

An interactive business intelligence dashboard built with Streamlit, analyzing the Global Superstore dataset to surface sales, profit, and customer insights through dynamic filters and visualizations.

 [View Project](https://github.com/ZareenAnsari/Interactive-Business-Dashboard-in-Streamlit)

## Overview

This dashboard lets users explore retail performance data interactively — filtering by region, category, and sub-category to instantly update KPIs and charts. Built as a hands-on data analytics project during a Data Science internship.

## Highlights

- 📊 Interactive filtering by Region, Category, and Sub-Category
- 💰 Real-time KPI metrics (Total Sales, Total Profit)
- 📈 Sales breakdown by region (bar chart)
- 📉 Profit breakdown by category (bar chart)
- 🏆 Top 5 customers by sales (bar chart)
- 🧹 Automated data cleaning (column normalization, duplicate removal, null handling)
- 🔍 Dynamic column detection for flexible dataset compatibility
- 🗂️ Live filtered dataset table view

## Tech Stack

- **Python**
- **Streamlit** — interactive web app framework
- **Pandas** — data cleaning and aggregation
- **Plotly Express** — interactive charts

## Dataset

The dashboard uses the **Global Superstore** dataset (`superstore.csv`), containing order-level retail data across regions, categories, sub-categories, and customers.

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/ZareenAnsari/Interactive-Business-Dashboard-in-Streamlit.git
cd Interactive-Business-Dashboard-in-Streamlit

# Install dependencies
pip install streamlit pandas plotly

# Run the app
streamlit run app.py
```

Make sure `superstore.csv` is in the same directory as the script before running.

## Project Structure

```
├── app.py                 # Main Streamlit dashboard script
├── superstore.csv          # Dataset
└── README.md
```

## Key Features Explained

- **Dynamic filters:** Sidebar lets users narrow the dataset by Region, Category, and Sub-Category (only shown if the column exists in the data).
- **KPI cards:** Total Sales and Total Profit update live based on active filters.
- **Visual breakdowns:** Separate charts for sales by region, profit by category, and top-performing customers.
- **Flexible column handling:** The script auto-detects sub-category and customer name columns to stay robust across slightly different dataset versions.
