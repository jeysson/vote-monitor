import csv
from typing import Iterable
from backend.domain.vote import Vote

def load_votes_from_csv(filepath: str) -> Iterable[Vote]:
    """Reads votes from a CSV file.
    Expected CSV header: id and bill_id
    """
    
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _id = int(row.get('id'))
            
            if not _id:
                continue

            yield Vote(
                    id=int(row['id']),
                    bill_id=int(row['bill_id'])
                )