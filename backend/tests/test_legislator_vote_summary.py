import tempfile
from backend.infrastructure.csv.csv_legislator_repository import CSVLegislatorRepository
from backend.infrastructure.csv.csv_vote_repository import CSVVoteRepository
from backend.infrastructure.csv.csv_vote_result_repository import CSVVoteResultRepository
from backend.services.vote_service import VoteService

LEG_CSV = """id,name
904789,Rep. Don Bacon (R-NE-2)
1603850,Rep. Jamaal Bowman (D-NY-16)
1852382,Rep. Cori Bush (D-MO-1)
904796,Rep. Brian Fitzpatrick (R-PA-1)
"""

VOTE_CSV = """id,bill_id
3314452,2900994
3321166,2952375
"""

VOTE_RESULT_CSV = """id,legislator_id,vote_id,vote_type
92516784,400440,3321166,2
92516770,17941,3321166,2
92516768,400414,3321166,2
92516640,904789,3321166,2
92516632,904796,3321166,2
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
    Test for every legislator available, how many bills did 
    the legislator support (voted forthe bill)?
    How many bills did the legislator oppose?
    Result expected: supported = 1, opposed = 2 for legislator with id
"""
def test_legislator_summary_supported_and_opposed():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as leg_csv:
        leg_csv.write(LEG_CSV)
        leg_csv.flush()

        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as vote_csv:
            vote_csv.write(VOTE_CSV)
            vote_csv.flush()

            with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as vote_result_csv:
                vote_result_csv.write(VOTE_RESULT_CSV)
                vote_result_csv.flush()

                legislator_repo = CSVLegislatorRepository(leg_csv.name)
                vote_repo = CSVVoteRepository(vote_csv.name)
                vote_result_repo = CSVVoteResultRepository(vote_result_csv.name)

                vote_service = VoteService(
                    legislator_repo=legislator_repo,
                    vote_repo=vote_repo,
                    vote_result_repo=vote_result_repo
                )

                summary = vote_service.get_legislator_summary(904789)

                assert summary['supported'] == 1
                assert summary['opposed'] == 2

