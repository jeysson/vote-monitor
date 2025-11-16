import csv
from typing import List, Optional
from backend.domain.bill import Bill
from backend.interfaces.bill_repository import BillRepository
from backend.infrastructure.csv.loaders.bill_loader import load_bills_from_csv

class CSVBillRepository(BillRepository):
    

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Bill]:
        return list(load_bills_from_csv(self.filepath))
        
    def get_by_id(self, id: int) -> Optional[Bill]:
        
        for bill in load_bills_from_csv(self.filepath):
            if bill.id == id:
                return bill
            
        return None