import pandas as pd

filename = 'excel_assessment.xlsx'
# filename = input("Enter the filename: ")


def read_excel_sheets():
    """
    Reads all sheets from an Excel file into a dictionary of DataFrames.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        dict: A dictionary where keys are sheet names and values are DataFrames.
    """
    excel_file = pd.ExcelFile(filename)
    sheet_names = excel_file.sheet_names
    all_data = {}

    try:
        for sheet_name in sheet_names:
            df = excel_file.parse(sheet_name)
            all_data[sheet_name] = df
    except FileNotFoundError:
        print("Error: Excel file not found.")
    except ValueError as e:
        print(f"Error: {e}")

    return all_data


def excel_to_csv():
    """
    Takes excel sheet and converts to multiple csv files placed in the project folder
    """
    all_sheets_data = read_excel_sheets()

    # Accessing individual DataFrames
    for sheet_name, df in all_sheets_data.items():
        df.to_csv(f"{sheet_name}.csv")

# excel_to_csv()