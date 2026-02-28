# Entry point for Retail Sales Summary Tool

#User Story 1 (Task 11)
from src.data_loader import load_data
from src.data_cleaning import convert_dates, handle_missing_values, validate_numeric_columns # data cleaning function
from src.sales_summary import total_sales
from src.sales_summary import sales_by_region

def main():
    try:
        # When you run: python3 src/main.py
        # the working folder is the project root, so use this path:
        df = load_data("data/superstore.csv")
        print("Data loaded successfully!")
        print("Number of rows:", len(df))
        print(df.head())
        print(100*"=")

        #clean data
        df = convert_dates(df)
        df = handle_missing_values(df)
        df = validate_numeric_columns(df)
        print("Data cleaned successfully!")
        print("Number of rows after cleaning:", len(df))
        print("Dataset After Cleaning:")
        print(df.head())
        print(100*"=")

        # Calculate total sales
        total = total_sales(df)
        print("Total sales:", total)
        print(100*"=")

        #Calculate sales by region
        region_sales = sales_by_region(df)
        print("Sales by Region:")
        print(region_sales)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()