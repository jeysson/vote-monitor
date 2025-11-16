import csv
from typing import List, Optional
from backend.domain.vote import Vote
from backend.interfaces.vote_repository import VoteRepository
from backend.infrastructure.csv.loaders.vote_loader import load_votes_from_csv

class CSVVoteRepository(VoteRepository):

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Vote]:
        return list(load_votes_from_csv(self.filepath))
    
    def get_by_id(self, id: int) -> Optional[Vote]:
        
        for vote in load_votes_from_csv(self.filepath):
            if vote.id == id:
                return vote
        return None
    
    def get_by_bill_id(self, bill_id: int) -> List[Vote]:
        votes: List[Vote] = []
        
        for vote in load_votes_from_csv(self.filepath):
            if vote.bill_id == bill_id:
                votes.append(vote)
        
        return votes