import csv
from typing import List, Optional
from backend.entities.legislator import Legislator
from backend.repositories.legislator_repository import LegislatorRepository

class CSVLegislatorRepository(LegislatorRepository):
    """Reads legislators from a CSV file.
    Expected CSV header: id,name
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Legislator]:
        legislators: List[Legislator] = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                legislator = Legislator(
                    id=int(row['id']),
                    name=row['name']
                )

                if legislator.id is not None:
                    legislators.append(legislator)    
                
        return legislators
    
    def get_by_id(self, id: int) -> Optional[Legislator]:
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['id']) == id:
                    return Legislator(
                        id=int(row['id']),
                        name=row['name']
                    )
        return None