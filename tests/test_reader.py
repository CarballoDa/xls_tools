import pandas as pd
import pytest
from xls_tools.reader import read_xls

# Puedes usar este archivo de ejemplo para tus pruebas
SAMPLE_FILE = "tests/sample.xlsx"

def test_read_excel_returns_dataframe():
    df = read_xls(SAMPLE_FILE)
    assert isinstance(df, pd.DataFrame), "Expected a DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_read_excel_invalid_path_returns_none():
    df = read_xls("tests/non_existent_file.xlsx")
    assert df is None, "Should return None for invalid file path"

def test_read_excel_specific_sheet():
    df = read_xls(SAMPLE_FILE, sheet_name=0)
    assert "Title" in df.columns, "Expected 'Title' in sheet"

def test_read_excel_specific_sheet_by_name():
    df = read_xls(SAMPLE_FILE, sheet_name="productos")
    assert "Title" in df.columns, "Title' in sheet"

def test_read_excel_invalid_sheet_name_returns_none():
    df = read_xls(SAMPLE_FILE, sheet_name="productos_reducidos")
    assert df is None, "Expected None when sheet name is invalid"
