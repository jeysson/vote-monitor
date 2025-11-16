import tempfile
from backend.infrastructure.csv.csv_vote_repository import CSVVoteRepository
from backend.infrastructure.csv.csv_legislator_repository import CSVLegislatorRepository
from backend.services.vote_service import VoteService

def test_vote_summary_for_legislator():
    # Legislators CSV
    legislators_csv = """id,name
    17941,Rep. Jeff Van Drew (R-NJ-2)
    400440,Rep. Don Young (R-AK-1)
    412211,Rep. John Yarmuth (D-KY-3)
    """

    # Votes CSV (3 votes to the legislator with id 17941)
    votes_csv = """id,bill_id
    1001,2001
    1002,2002
    1003,2003
    """

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as leg_file_csv:
        leg_file_csv.write(legislators_csv)
        leg_file_csv.flush()

        with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as vote_file_csv:
            vote_file_csv.write(votes_csv)
            vote_file_csv.flush()

            # Setup repositories and service
            legislator_repo = CSVLegislatorRepository(filepath=leg_file_csv.name)  # IGNORE
            vote_repo = CSVVoteRepository(filepath=vote_file_csv.name)
            vote_service = VoteService(legislator_repository=legislator_repo,
                                        vote_repository=vote_repo)

            # Fetch votes
            summary = vote_service.get_legislator_vote_summary(17941)
            assert summary['id'] == 17941
            assert summary['name'] == "Rep. Jeff Van Drew (R-NJ-2)"
            assert summary['supported'] == 1 # yes
            assert summary['opposed'] == 2    # no