import csv
from typing import List, Optional
from backend.entities.bill import Bill
from backend.repositories.bill_repository import BillRepository

class CSVBillRepository(BillRepository):
    """Reads bills from a CSV file.
    Expected CSV header: id, title and sponsor_id
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Bill]:
        bills: List[Bill] = []

        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                bill = Bill(
                    id=int(row['id']),
                    title=row['title'],
                    sponsor_id=int(row['sponsor_id'])
                )

                if bill.id is not None:
                    bills.append(bill)    
                
        return bills
    
    def get_by_id(self, id: int) -> Optional[Bill]:
        
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                if int(row['id']) == id:
                    return Bill(
                        id=int(row['id']),
                        title=row['title'],
                        sponsor_id=int(row['sponsor_id'])
                    )
        return None