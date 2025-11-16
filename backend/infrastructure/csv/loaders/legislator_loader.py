import csv
from typing import Iterable
from backend.domain.legislator import Legislator

def load_legislators_from_csv(filepath: str) -> Iterable[Legislator]:
    """Reads legislators from a CSV file.
    Expected CSV header: id,name
    """
    
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _id = int(row.get('id'))
            
            if not _id:
                continue

            yield Legislator(
                    id=int(row['id']),
                    name=row['name']
                )