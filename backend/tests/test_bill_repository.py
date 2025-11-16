import tempfile
from backend.infrastructure.csv.csv_bill_repository import CSVBillRepository

CSV_CONTENT = """id,title,sponsor_id
2952375,H.R. 5376: Build Back Better Act,412211
2900994,H.R. 3684: Infrastructure Investment and Jobs Act,400100
"""

"""
    Test get all bills from CSVBillRepository
    Result expected: 2 bills in total
"""
def test_get_all():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVBillRepository(filepath=file_csv.name)

        all_bills = repo.get_all()
        # Total 2 bills in the CSV
        assert len(all_bills) == 2
        

"""
    Test get bill by id from CSVBillRepository
    Result expected: Legislator with id 904789 and name Rep. Don Bacon (R-NE-2)
"""
def test_get_by_id():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVBillRepository(filepath=file_csv.name)

        bill = repo.get_by_id(2952375)        
        
        assert bill is not None
        assert bill.id == 2952375
        assert bill.title == "H.R. 5376: Build Back Better Act"
        assert bill.sponsor_id == 412211