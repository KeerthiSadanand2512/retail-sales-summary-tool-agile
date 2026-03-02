from src.data_loader import load_data
from src.data_cleaning import convert_dates, handle_missing_values, validate_numeric_columns
from src.sales_summary import sales_summary_report
from src.profit_analysis import profit_report
from src.customer_performance import total_sales_per_customer, top_10_customers


def main():
    try:    
        # When you run: python3 src/main.py 
        # the working folder is the project root, so use this path:

        # Data Loading
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

        # Sales Summary Report
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


        # Profit Analysis Report
        report = profit_report(df)

        # ---- validations ----
        
        assert isinstance(report["total_profit"], float)

        assert not report["profit_by_category"].empty
        assert "Category" in report["profit_by_category"].columns
        assert "Total Profit" in report["profit_by_category"].columns

        assert not report["profit_by_sub_category"].empty
        assert "Sub-Category" in report["profit_by_sub_category"].columns
        assert "Total Profit" in report["profit_by_sub_category"].columns
       
        # ---- Print Results ----
        print("Profit Report Generated Successfully")
        print("Total Profit:", report["total_profit"])
        print(100*"=")

        print("\nProfit by Category (Top 5):")
        print(report["profit_by_category"].head(5))
        print(100*"=")

        print("\nProfit by Sub-Category (Top 5):")
        print(report["profit_by_sub_category"].head(5))
        print(100*"=")

        # --- Customer Performance  ---
        customer_sales = total_sales_per_customer(df)
        print("=== Total Sales per Customer (Top 5 Preview) ===")
        print(customer_sales.head())
        print(100 * "=")

        top_customers = top_10_customers(df)
        print("=== Top 10 Customers by Total Sales ===")
        print(top_customers)
        print(100 * "=")



        # Catch any unexpected exceptions to prevent crashing and provide feedback
    except Exception as e:
        print("Error:", e)

    


if __name__ == "__main__":
    main()

