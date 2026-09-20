# E-commerce Sales Data Engineering Practice

## 📌 About This Practice Project

This is a hands-on practice project created to learn and apply basic Data Engineering concepts using Python, Pandas, PySpark, and Databricks.

In this project, I worked with a small e-commerce sales dataset and practiced data cleaning, transformation, aggregation, ETL concepts, and data visualization.

## 🛠️ Technologies Used

- Python
- Pandas
- PySpark
- Databricks
- Delta Lake
- CSV

## 🔄 Practice Workflow

Raw CSV Data  
↓  
Pandas Data Analysis  
↓  
Data Cleaning  
↓  
PySpark ETL in Databricks  
↓  
Data Transformation  
↓  
Sales Analysis  
↓  
Delta Table  
↓  
Visualizations

## 🧹 Data Cleaning Practice

The following data-cleaning tasks were practiced:

- Loaded CSV data using Pandas
- Checked dataset structure and information
- Checked missing values
- Identified duplicate records
- Removed duplicate records
- Converted Order_Date to date format
- Converted Quantity and Price to appropriate data types

## ⚙️ PySpark & Databricks Practice

The following Data Engineering concepts were practiced in Databricks:

- Reading CSV data using PySpark
- Removing duplicate records
- Data type conversion
- Creating a Revenue column
- Product-wise revenue aggregation
- City-wise revenue aggregation
- Total revenue calculation
- Finding the best-selling product by quantity
- Saving processed data as a Delta table
- Creating basic visualizations

Revenue was calculated as:

Revenue = Quantity × Price

## 📊 Practice Results

- Raw records: 12
- Records after removing duplicates: 11
- Total Revenue: ₹3,94,900
- Highest revenue product: Laptop
- Highest quantity sold product: Mouse
- Highest revenue city: Delhi

## 📈 Visualizations

### Product-wise Revenue

![Product Revenue](Visualization/product_revenue.png)

### City-wise Revenue

![City Revenue](Visualization/city_revenue.png)

## 📁 Project Structure

```text
Ecommerce-Sales-Data-Engineering/
│
├── Databricks/
│   └── Ecommerce_Sales_ETL.ipynb
│
├── Data/
│   └── sales.csv
│
├── Pandas/
│   └── analysis.py
│
└── Visualization/
    ├── product_revenue.png
    └── city_revenue.png
