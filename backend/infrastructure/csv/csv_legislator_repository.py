import csv
from typing import List, Optional
from backend.domain.legislator import Legislator
from backend.interfaces.legislator_repository import LegislatorRepository
from backend.infrastructure.csv.loaders.legislator_loader import load_legislators_from_csv

class CSVLegislatorRepository(LegislatorRepository):


    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Legislator]:
        return list(load_legislators_from_csv(self.filepath))
    
    def get_by_id(self, id: int) -> Optional[Legislator]:
        for legislator in load_legislators_from_csv(self.filepath):
            if legislator.id == id:
                return legislator
            
        return None