from backend.interfaces.bill_repository import BillRepository
from backend.interfaces.vote_repository import VoteRepository
from backend.interfaces.vote_result_repository import VoteResultRepository
from backend.interfaces.legislator_repository import LegislatorRepository
from backend.domain.bill_summary import BillSummary

class BillVoteSummaryService:

    def __init__(self, bill_repo: BillRepository, 
                 legislator_repo: LegislatorRepository, 
                 vote_repo: VoteRepository, 
                 vote_result_repo: VoteResultRepository):
        self.bill_repo = bill_repo
        self.legislator_repo = legislator_repo
        self.vote_repo = vote_repo
        self.vote_result_repo = vote_result_repo

    def get_bill_summary(self, bill_id: int) -> BillSummary:
        bill = self.bill_repo.get_by_id(bill_id)
        if not bill:
            return None

        votes = self.vote_repo.get_by_bill_id(bill_id)
        vote_ids = [vote.id for vote in votes]

        results = self.vote_result_repo.get_by_vote_ids(vote_ids)

        supporters = sum(1 for r in results if r.vote_type == 1)
        opposers = sum(1 for r in results if r.vote_type == 2)

        sponsor = self.legislator_repo.get_by_id(bill.sponsor_id)

        return BillSummary(
            bill_id=bill.id,
            bill_title=bill.title,
            supporters=supporters,
            opposers=opposers,
            primary_sponsor=sponsor.name if sponsor else "Unknown"
        )
