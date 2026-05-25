import json
import csv
import os

class StorageManager:
    DATA_FILE = 'data.json'
    EXPORT_FILE = 'export.csv'

    @classmethod
    def load_data(cls):
        """Loads expense data from the JSON file."""
        if not os.path.exists(cls.DATA_FILE):
            return []
        try:
            with open(cls.DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    @classmethod
    def save_data(cls, data):
        """Saves expense data to the JSON file."""
        with open(cls.DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def export_csv(cls, data):
        """Exports current data to a CSV file. Returns True if successful."""
        if not data:
            return False
            
        with open(cls.EXPORT_FILE, 'w', newline='') as f:
            fieldnames = ["date", "category", "description", "amount"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True