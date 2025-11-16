import csv
from typing import List, Optional
from backend.domain.vote_result import VoteResult
from backend.interfaces.vote_result_repository import VoteResultRepository
from backend.infrastructure.csv.loaders.vote_result_loader import load_vote_results_from_csv

class CSVVoteResultRepository(VoteResultRepository):

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[VoteResult]:
        return list(load_vote_results_from_csv(self.filepath))
    
    def get_by_id(self, id: int) -> Optional[VoteResult]:
        
        for voteResult in load_vote_results_from_csv(self.filepath):
            if voteResult.id == id:
                return voteResult
            
        return None
    
    def get_by_legislator_id(self, legislator_id: int) -> List[VoteResult]:
        votesResult: List[VoteResult] = []
        
        for voteResult in load_vote_results_from_csv(self.filepath):
            if voteResult.legislator_id == legislator_id:
                votesResult.append(voteResult)
        
        return votesResult
    
    def get_by_vote_id(self, vote_id) -> List[VoteResult]:
        votesResult: List[VoteResult] = []
        
        for voteResult in load_vote_results_from_csv(self.filepath):
            if voteResult.vote_id == vote_id:
                votesResult.append(voteResult)
        
        return votesResult
    
    def get_by_vote_ids(self, vote_ids: List[int]) -> List[VoteResult]:
        votesResult: List[VoteResult] = []
        
        for voteResult in load_vote_results_from_csv(self.filepath):
            if voteResult.vote_id in vote_ids:
                votesResult.append(voteResult)
        
        return votesResult