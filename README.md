# 🍔 Fast Food Order Analysis & Billing System

A Python and Pandas-based data analysis project that automates fast-food order management, data cleaning, sales analysis, and customer billing.

## 📌 Project Overview

Fast-food businesses generate large amounts of transaction data every day. Managing these records manually can lead to missing information, duplicate transactions, billing errors, and difficulties in identifying sales trends.

This project provides an end-to-end solution using Python and Pandas to clean, combine, analyze, and transform raw order data into meaningful business insights. It also includes an interactive terminal-based ordering and billing system.

## 🎯 Objectives

- Load and combine multi-day order datasets.
- Clean missing values and duplicate records.
- Handle inconsistent data and incorrect data types.
- Calculate order totals and apply discount rules.
- Analyze sales, payment preferences, and product performance.
- Identify menu items that received no orders.
- Generate customer bills through an interactive terminal interface.
- Export processed datasets into CSV files.

## 🛠️ Technologies Used

- Python
- Pandas
- CSV Data Handling
- Jupyter Notebook / Python IDE

## 📂 Project Structure

```text
Fast-Food-Order-Analysis/
│
├── main.py
├── menu.csv
├── orders_friday.csv
├── orders_saturday.csv
├── final_cleaned_orders.csv
├── order_totals.csv
├── requirements.txt
├── README.md
└── screenshots/
```

## 📊 Datasets

| File | Description |
|---|---|
| menu.csv | Restaurant menu and product information |
| orders_friday.csv | Friday transaction records |
| orders_saturday.csv | Saturday transaction records |

## 🧹 Data Cleaning & Preprocessing

The following operations were performed:

- `dropna()` to remove records with missing critical identifiers.
- `fillna()` to handle missing payment modes and quantities.
- `interpolate()` to estimate missing delivery times.
- `drop_duplicates()` to remove duplicate transactions.
- Data type conversion for quantity columns.
- Removal of unnecessary columns.

## 📈 Data Analysis & Feature Engineering

The project uses Pandas operations including:

- `pd.concat()` to combine daily order datasets.
- `pd.merge()` to join order records with menu information.
- `groupby()` for category and payment analysis.
- `sort_values()` to rank transaction amounts.
- `agg()` for multiple statistical calculations.
- Filtering and conditional selection.
- Feature engineering for line totals, size tags, and discounts.

## 💰 Billing & Discount System

The system calculates order totals and applies the following discount rules:

| Order Amount | Discount |
|---|---:|
| Rs. 3,000 or above | 10% |
| Rs. 1,500 or above | 5% |
| Below Rs. 1,500 | No discount |

## 🔍 Key Business Insights

- Identifies the highest revenue-generating food item.
- Calculates sales across different food categories.
- Analyzes cash and card payment preferences.
- Identifies large transactions.
- Finds menu items that received zero orders.
- Generates customer bills with applicable discounts.

## 📁 Output Files

- `final_cleaned_orders.csv` — Cleaned and processed transaction records.
- `order_totals.csv` — Order-wise calculated totals.

## ⚙️ Installation & Execution

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd fast-food-order-analysis-and-billing-system
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python main.py
```

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and Pandas.
- Real-world data cleaning and preprocessing.
- Data manipulation and feature engineering.
- Data aggregation and business analysis.
- Relational data merging.
- CSV file handling.
- Building a terminal-based billing application.

## 👩‍💻 Author

**Esha Rani**

Computer Science Student

GitHub: https://github.com/asifkhanas1206-stack

---

*This project was developed as a practical demonstration of Python and Pandas concepts applied to a real-world business scenario.*
