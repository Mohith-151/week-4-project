# WEEK-4 Project: Monthly Expense Analysis 📊

## Overview

This project is a data analysis and visualization exercise focused on tracking and understanding personal monthly expenses. Using Python, Pandas, and Matplotlib, the project processes raw CSV data to uncover spending patterns—specifically comparing expenses made alone versus those made with friends.

---

## Project Structure

```text
WEEK 4/
├── data/
│   └── myExpenses1.csv
├── hands on practice/
├── report/
│   └── report.pdf
├── visualizations/
│   ├── barChart.png
│   └── PieChart.png
├── analysis.ipynb
└── requirements.txt
```

---

## Dataset & Data Cleaning

The analysis uses a local dataset (`data/myExpenses1.csv`) which initially contained **145 entries**.

**Features tracked:** `Date`, `Item`, `Amount`, `Category`, `Time`, and `day`.

**Data Cleaning:** During the initial inspection, one row *(Index 72, Date: 12/3/2023)* containing a missing (NULL) value in the `Category` column was identified. This row was dropped to ensure accurate calculations, leaving a clean dataset of **144 entries** for analysis.

---

## Key Insights

The notebook calculates several important financial metrics from the cleaned data:

| Metric | Value |
|---|---|
| Total Spent | ₹4,599 |
| Average Spent per Transaction | ₹31.94 |
| Spent Alone | ₹2,710 (58.9%) |
| Spent with Friends | ₹1,889 (41.1%) |

### Category Breakdown

- **58.9%** of the budget was spent while **alone** (Total: ₹2,710)
- **41.1%** of the budget was spent with **friends** (Total: ₹1,889)

---

## Top 3 Highest Spent Items

### 🧍 When Alone

| Rank | Item | Amount |
|---|---|---|
| 1 | Chai with snacks | ₹1,065 |
| 2 | Shoe | ₹500 |
| 3 | Wi-Fi | ₹350 |

### 👥 With Friends

| Rank | Item | Amount |
|---|---|---|
| 1 | Biryani | ₹580 |
| 2 | Juice | ₹195 |
| 3 | Chicken | ₹180 |

---

## Visualizations

The analysis outputs two primary visual plots using Matplotlib, saved in the `visualizations/` folder:

1. **Bar Chart** (`barChart.png`) — A side-by-side comparison of the top 3 highest spent items between the *Alone* and *Friends* categories.
2. **Pie Chart** (`PieChart.png`) — Illustrates the overall percentage split of total expenses by category.

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "WEEK 4"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the notebook**
   ```bash
   jupyter notebook analysis.ipynb
   ```

4. **Run all cells** — The notebook will load the dataset, clean the data, compute the metrics, and save the visualizations to the `visualizations/` folder.

---

## Requirements

All dependencies are listed in `requirements.txt`. Key libraries used:

- `pandas` — Data loading, cleaning, and analysis
- `matplotlib` — Chart and plot generation
- `jupyter` — Interactive notebook environment

---
