import tempfile
from backend.infrastructure.csv.csv_vote_repository import CSVVoteRepository

CSV_CONTENT = """id,bill_id
3314452,2900994
3321166,2952375
"""

"""
    Test get all votes from CSVVoteRepository
    Result expected: 2 votes in total
"""
def test_get_all():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVVoteRepository(filepath=file_csv.name)

        all_bills = repo.get_all()
        # Total 2 bills in the CSV
        assert len(all_bills) == 2
        

"""
    Test get vote by id from CSVVoteRepository
    Result expected: Vote with id 3314452 and bill_d 2900994
"""
def test_get_by_id():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as file_csv:
        file_csv.write(CSV_CONTENT)
        file_csv.flush()

        repo = CSVVoteRepository(filepath=file_csv.name)

        vote = repo.get_by_id(3314452)        
        
        assert vote is not None
        assert vote.id == 3314452
        assert vote.bill_id == 2900994