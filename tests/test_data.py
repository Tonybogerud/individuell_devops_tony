import csv
import json

def test_csv_column_count():
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert len(headers) == 12

def test_csv_row_count():
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) > 900  # includes header

def test_json_row_count():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) > 900

def test_json_properties():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert all(len(item) == 12 for item in data)
