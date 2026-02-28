from src.data_loader import load_data
from src.data_cleaning import convert_dates, handle_missing_values, validate_numeric_columns
from src.sales_summary import sales_summary_report


def main():
    try:
        # When you run: python3 src/main.py 
        # the working folder is the project root, so use this path:
        df = load_data("data/superstore.csv")
        print("Data loaded successfully!")
        print("Number of rows:", len(df))
        print(df.head())
        print(100*"=")

        df = convert_dates(df)
        df = handle_missing_values(df)
        df = validate_numeric_columns(df)
        print("Data cleaned successfully!")
        print("Number of rows after cleaning:", len(df))
        print(df.head())
        print(100*"=")

        report = sales_summary_report(df)

        print("=== Total Sales ===")
        print(report["total_sales"])
        print(100*"=")

        print("=== Sales by Region ===")
        print(report["sales_by_region"])
        print(100*"=")

        print("=== Sales by Category ===")
        print(report["sales_by_category"])
        print(100*"=")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()