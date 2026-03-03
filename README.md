# Retail Sales Summary Tool – Agile Sprint

This project was developed as part of the Agile module for the Masters in Data Analytics program.

## Sprint Goal
Deliver a modular Python tool that generates key retail insights from the Superstore dataset using Agile collaboration practices.
## Sprint Goal

The goal of this sprint was to design and implement a modular Retail Sales Summary Tool using Agile principles.

The sprint focused on:

- Building a clean, reusable Python architecture
- Separating logic from presentation (no print statements inside modules)
- Implementing structured outputs (DataFrames, floats, dictionaries)
- Ensuring maintainability through standardized docstrings and type annotations
- Applying proper Git branching and Pull Request workflow

By the end of the sprint, the system successfully:
- Loads and cleans the Superstore dataset
- Generates sales summary insights
- Performs profit analysis
- Identifies top-performing customers
- Maintains a fully modular and documented code structure

## Project Structure
## Project Structure


retail-sales-summary-tool-agile/
│
├── main.py # Entry point of the application
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── data/
│ └── superstore.csv # Input dataset
│
└── src/
├── init.py # Marks src as a Python package
├── data_loader.py # Handles loading CSV data
├── data_cleaning.py # Handles cleaning and validation
├── sales_summary.py # Sales analysis functions
├── profit_analysis.py # Profit analysis functions
└── customer_performance.py # Customer sales insights

### Module Responsibilities

- **data_loader.py** → Loads dataset safely with validation
- **data_cleaning.py** → Cleans dates, missing values, and numeric validation
- **sales_summary.py** → Computes sales-related summaries
- **profit_analysis.py** → Computes profit-related insights
- **customer_performance.py** → Identifies top-performing customers
- **main.py** → Orchestrates execution and prints results


## How to Run

Follow these steps to execute the project:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd retail-sales-summary-tool-agile

## Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

## Install Required Packages
pip install -r requirements.txt

## Run the Application
python3 main.py
