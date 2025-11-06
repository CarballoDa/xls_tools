import pandas as pd
from pandas.errors import EmptyDataError
from openpyxl.utils.exceptions import InvalidFileException

def read_xls(file_path: str, sheet_name=0):
    '''Reading xlsx file and returning a Dataframe'''
    try:
        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
        return dataframe
    except FileNotFoundError:
        print(f"Error: path or file not found -> {file_path}")
    except ValueError as ve:
        print(f"Error: Sheet name or Index invalid -> {ve}")
    except EmptyDataError:
        print(f"Error: Excel file is empty")
    except InvalidFileException:
        print(f"Error: Invalid excel file format -> {file_path}")
    except Exception as e:
        print(f"Error: exception reading file -> {e}")