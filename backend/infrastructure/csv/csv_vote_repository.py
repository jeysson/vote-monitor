import csv
from typing import List, Optional
from backend.entities.vote import Vote
from backend.repositories.vote_repository import VoteRepository

class CSVVoteRepository(VoteRepository):
    """Reads votes from a CSV file.
    Expected CSV header: id and bill_id
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_all(self) -> List[Vote]:
        votes: List[Vote] = []

        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                vote = Vote(
                    id=int(row['id']),
                    bill_id=int(row['bill_id'])
                )

                if vote.id is not None:
                    votes.append(vote)    
                
        return votes
    
    def get_by_id(self, id: int) -> Optional[Vote]:
        
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                if int(row['id']) == id:
                    return Vote(
                        id=int(row['id']),
                        bill_id=int(row['bill_id'])
                    )
        return None