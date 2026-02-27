# Entry point for Retail Sales Summary Tool

#User Story 1 (Task 11)
from data_loader import load_data


def main():
    try:
        # When you run: python3 src/main.py
        # the working folder is the project root, so use this path:
        df = load_data("data/superstore.csv")

        print("Data loaded successfully!")
        print("Number of rows:", len(df))
        print(df.head())
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()