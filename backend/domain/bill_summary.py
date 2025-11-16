from dataclasses import dataclass

@dataclass
class BillSummary:
    bill_id: int
    bill_title: str
    supporters: int
    opposers: int
    primary_sponsor: str
