import csv
from typing import Iterable
from backend.domain.vote_result import VoteResult

def load_vote_results_from_csv(filepath: str) -> Iterable[VoteResult]:
    """Reads voteResult from a CSV file.
    Expected CSV header: id, legislator_id, vote_id and vote_type
    """
    
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _id = int(row.get('id'))
            
            if not _id:
                continue

            yield VoteResult(
                    id=int(row['id']),
                    legislator_id=int(row['legislator_id']),
                    vote_id=int(row['vote_id']),
                    vote_type=int(row['vote_type'])
                )