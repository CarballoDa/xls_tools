import pandas as pd
import pytest
from xls_tools.reader import read_xls

# Puedes usar este archivo de ejemplo para tus pruebas
SAMPLE_FILE = "tests/sample.xlsx"
SAMPLE_EMPTY_FILE = "tests/empty_sample.xlsx"
SAMPLE_NONEXISTENT_FILE = "tests/non_existent_sample.xlsx"

def test_read_excel_returns_dataframe():
    df = read_xls(SAMPLE_FILE)
    assert isinstance(df, pd.DataFrame), "Expected a DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_read_xls_invalid_path_returns_none():
    df = read_xls(SAMPLE_NONEXISTENT_FILE)
    assert df is None, "Should return None for invalid file path"

def test_read_xls_specific_sheet():
    df = read_xls(SAMPLE_FILE, sheet_name=0)
    assert "Title" in df.columns, "Expected 'Title' in sheet"

def test_read_xls_specific_sheet_by_name():
    df = read_xls(SAMPLE_FILE, sheet_name="Products")
    assert "Title" in df.columns, "Title' in sheet"

def test_read_xls_invalid_sheet_name_returns_none():
    df = read_xls(SAMPLE_FILE, sheet_name="nosheet")
    assert df is None, "Expected None when sheet name is invalid"

def test_read_xls_file_not_found():
    df = read_xls(SAMPLE_NONEXISTENT_FILE, sheet_name="nonexistent_sheet")
    assert df is None

def test_read_xls_inavlid_sheet_name():
    df = read_xls(SAMPLE_FILE, sheet_name="nonexistent_sheet")
    assert df is None

def test_read_xls_empty():
    df = read_xls(SAMPLE_EMPTY_FILE)
    assert df.empty, "Expected empty DataFrame"

def test_read_xls_invalid_file_extension():
    df = read_xls("tests/sample.pdf")
    assert df is None