from typing import List, Dict
from backend.interfaces.vote_repository import VoteRepository
from backend.interfaces.vote_result_repository import VoteResultRepository
from backend.interfaces.legislator_repository import LegislatorRepository

class VoteService:

    def __init__(self, vote_repo: VoteRepository,
                 vote_result_repo: VoteResultRepository,
                 legislator_repo: LegislatorRepository):
        self.vote_repo = vote_repo
        self.vote_result_repo = vote_result_repo
        self.leg_repo = legislator_repo
        

    def get_votes_by_legislator(self, legislator_id: int) -> List[Dict]:
        """Return list of records: {legislator_id, bill_id, vote_type}"""
        
        votesResult = self.vote_result_repo.get_by_legislator_id(legislator_id)

        results = []
        
        for voteResult in votesResult:
            vote = self.vote_repo.get_by_id(voteResult.vote_id)

            if vote is None:
                continue

            results.append({
                'legislator_id': legislator_id,
                'bill_id': vote.bill_id,
                'vote_type': voteResult.vote_type
            })


        return results

    def get_legislator_summary(self, legislator_id: int) -> Dict[str, int]:
        """Return summary of votes by a legislator:
        {legislator_id, legislator_name, total_votes, yes_votes, no_votes, abstain_votes}
        """

        records = self.get_votes_by_legislator(legislator_id)
        supported = sum(1 for record in records if record['vote_type'] == 1)
        opposed = sum(1 for record in records if record['vote_type'] == 2)

        return { "supported": supported, "opposed": opposed }
    
    def get_all_legislator_summaries(self) -> List[Dict]:
        """Return list of summaries for all legislators."""

        legislators = self.leg_repo.get_all()
        summaries = []

        for legislator in legislators:
            summary = self.get_legislator_summary(legislator.id)
            summary['legislator_id'] = legislator.id
            summary['legislator_name'] = legislator.name
            summaries.append(summary)

        return summaries