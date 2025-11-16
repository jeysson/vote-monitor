import tempfile

from backend.infrastructure.csv.csv_bill_repository import CSVBillRepository
from backend.infrastructure.csv.csv_legislator_repository import CSVLegislatorRepository
from backend.infrastructure.csv.csv_vote_repository import CSVVoteRepository
from backend.infrastructure.csv.csv_vote_result_repository import CSVVoteResultRepository
from backend.services.bill_vote_service import BillVoteService

CSV_BILLS = """id,title,sponsor_id
2952375,H.R. 5376: Build Back Better Act,1603850
2900994,H.R. 3684: Infrastructure Investment and Jobs Act,904796
"""

CSV_LEGISLATORS = """id,name
904789,Rep. Don Bacon (R-NE-2)
1603850,Rep. Jamaal Bowman (D-NY-16)
1852382,Rep. Cori Bush (D-MO-1)
904796,Rep. Brian Fitzpatrick (R-PA-1)
"""

CSV_VOTES = """id,bill_id
3314452,2900994
3321166,2952375
"""

CSV_VOTE_RESULTS = """id,legislator_id,vote_id,vote_type
92516784,400440,3321166,2
92516770,17941,3321166,2
92516768,400414,3321166,1
92516640,904789,3321166,1
92516632,904796,3321166,1
92516579,904789,3321166,2
92516553,1269790,3321166,1
92516513,1269778,3321166,1
92516500,905216,3321166,1
92516499,1269767,3321166,1
92516373,904789,3321166,1
92516368,1603850,3321166,1
92280168,1269790,3314452,2
92280136,1269778,3314452,2
92280128,905216,3314452,2
92280127,1269767,3314452,2
"""

"""
    Test get bill vote summary from BillVoteSummaryService
    Result expected: supporters = 9, opposers = 3 for bill with id
"""
def test_bill_vote_summary():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as leg_csv:
        leg_csv.write(CSV_LEGISLATORS)
        leg_csv.flush()

        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as bill_csv:
            bill_csv.write(CSV_BILLS)
            bill_csv.flush()

            with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as vote_csv:
                vote_csv.write(CSV_VOTES)
                vote_csv.flush()

                with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as vote_result_csv:
                    vote_result_csv.write(CSV_VOTE_RESULTS)
                    vote_result_csv.flush()


                    bill_repo = CSVBillRepository(bill_csv.name)
                    legislator_repo = CSVLegislatorRepository(leg_csv.name)
                    vote_repo = CSVVoteRepository(vote_csv.name)
                    vote_result_repo =  CSVVoteResultRepository(vote_result_csv.name)

                    service = BillVoteService(
                        bill_repo=bill_repo,
                        legislator_repo=legislator_repo,
                        vote_repo=vote_repo,
                        vote_result_repo=vote_result_repo
                    )

                    summary = service.get_bill_summary(2952375)

                    assert summary.bill_id == 2952375
                    assert summary.bill_title == "H.R. 5376: Build Back Better Act"
                    assert summary.supporters == 9
                    assert summary.opposers == 3
                    assert summary.primary_sponsor == "Rep. Jamaal Bowman (D-NY-16)"
