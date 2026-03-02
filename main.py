from src.data_loader import load_data
from src.data_cleaning import convert_dates, handle_missing_values, validate_numeric_columns
from src.sales_summary import sales_summary_report
from src.profit_analysis import profit_report
from src.customer_performance import total_sales_per_customer, top_10_customers


def main() -> None:
    try:
        # Data Loading
        df = load_data("data/superstore.csv")
        print("Data loaded successfully!")
        print("Number of rows:", len(df))
        print(df.head())
        print(100 * "=")

        # Data Cleaning
        df = convert_dates(df)
        df = handle_missing_values(df)
        df = validate_numeric_columns(df)
        print("Data cleaned successfully!")
        print("Number of rows after cleaning:", len(df))
        print(df.head())
        print(100 * "=")

        # Sales Summary Report
        sales_report = sales_summary_report(df)

        print("=== Total Sales ===")
        print(sales_report["total_sales"])
        print(100 * "=")

        print("=== Sales by Region ===")
        print(sales_report["sales_by_region"])
        print(100 * "=")

        print("=== Sales by Category ===")
        print(sales_report["sales_by_category"])
        print(100 * "=")

        # Profit Analysis Report
        profit_report_data = profit_report(df)

        # ---- validations ----
        assert isinstance(profit_report_data, dict), "Profit report must be a dictionary"

        assert isinstance(profit_report_data["total_profit"], float), "total_profit must be float"

        assert not profit_report_data["profit_by_category"].empty, "profit_by_category is empty"
        assert "Category" in profit_report_data["profit_by_category"].columns
        assert "Total Profit" in profit_report_data["profit_by_category"].columns

        assert not profit_report_data["profit_by_sub_category"].empty, "profit_by_sub_category is empty"
        assert "Sub-Category" in profit_report_data["profit_by_sub_category"].columns
        assert "Total Profit" in profit_report_data["profit_by_sub_category"].columns

        # ---- Print Results ----
        print("=== Profit Report Generated Successfully ===")
        print("Total Profit:", profit_report_data["total_profit"])
        print(100 * "=")

        print("=== Profit by Category (Top 5) ===")
        print(profit_report_data["profit_by_category"].head(5))
        print(100 * "=")

        print("=== Profit by Sub-Category (Top 5) ===")
        print(profit_report_data["profit_by_sub_category"].head(5))
        print(100 * "=")

        # Customer Performance Report
        print("=== Total Sales per Customer (Top 5) ===")
        sales_customer = total_sales_per_customer(df)
        print(sales_customer.head(5))
        print(100 * "=")

        print("=== Top 10 Customers by Total Sales ===")
        print(top_10_customers(df))
        print(100 * "=")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()