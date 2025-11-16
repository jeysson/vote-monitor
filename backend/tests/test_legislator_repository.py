import tempfile
from backend.infrastructure.csv.csv_legislator_repository import CSVLegislatorRepository

CSV_CONTENT = """id,name
904789,Rep. Don Bacon (R-NE-2)
1603850,Rep. Jamaal Bowman (D-NY-16)
1852382,Rep. Cori Bush (D-MO-1)
904796,Rep. Brian Fitzpatrick (R-PA-1)
"""

"""
    Test get all legislators from LegislatorRepository
    Result expected: 4 legislators
"""
def test_get_all():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVLegislatorRepository(filepath=file_csv.name)

        all_congressistas = repo.get_all()
        # Total 4 legislator in the CSV
        assert len(all_congressistas) == 4
        # Check one legislator
        congressista = repo.get_by_id(1603850)
        assert congressista is not None
        assert congressista.id == 1603850
        assert congressista.name == "Rep. Jamaal Bowman (D-NY-16)"

"""
    Test get legislator by id from LegislatorRepository
    Result expected: Legislator with id 904789 and name Rep. Don Bacon (R-NE-2)
"""
def test_get_by_id():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVLegislatorRepository(filepath=file_csv.name)

        legislator = repo.get_by_id(904789)        
        
        assert legislator is not None
        assert legislator.id == 904789
        assert legislator.name == "Rep. Don Bacon (R-NE-2)"