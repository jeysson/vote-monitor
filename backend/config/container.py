from backend.config.settings import settings
from backend.infrastructure.csv.csv_legislator_repository import CSVLegislatorRepository
from backend.infrastructure.csv.csv_bill_repository import CSVBillRepository
from backend.infrastructure.csv.csv_vote_repository import CSVVoteRepository
from backend.infrastructure.csv.csv_vote_result_repository import CSVVoteResultRepository

from backend.services.bill_vote_service import BillVoteService
from backend.services.vote_service import VoteService


class Container:
    # Repositories
    legislators_repo = CSVLegislatorRepository(settings.data.legislators)
    bills_repo = CSVBillRepository(settings.data.bills)
    votes_repo = CSVVoteRepository(settings.data.votes)
    vote_results_repo = CSVVoteResultRepository(settings.data.vote_results)

    # Services
    legislator_summary_service = VoteService(
        legislator_repo=legislators_repo,
        vote_repo=votes_repo,
        vote_result_repo=vote_results_repo
    )

    bill_summary_service = BillVoteService(
        bill_repo=bills_repo,
        legislator_repo=legislators_repo,
        vote_repo=votes_repo,
        vote_result_repo=vote_results_repo
    )


container = Container()
