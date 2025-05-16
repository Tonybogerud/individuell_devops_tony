import csv
import json

print("🚀 Script started")

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"{len(data)} rows converted from {csv_file} to {json_file}")

if __name__ == "__main__":
    convert_csv_to_json('profiles1.csv', 'data.json')
    print("✅ Script finished")
