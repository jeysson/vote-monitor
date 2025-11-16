import csv
from typing import Iterable
from backend.domain.bill import Bill

def load_bills_from_csv(filepath: str) -> Iterable[Bill]:
    """Reads bills from a CSV file.
    Expected CSV header: id, title and sponsor_id
    """
    
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _id = int(row.get('id'))
            
            if not _id:
                continue

            yield Bill(
                id=int(row['id']),
                title=row['title'],
                sponsor_id=int(row['sponsor_id'])
            )