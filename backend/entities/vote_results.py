from dataclasses import dataclass

@dataclass
class VoteResults:
    # The id of the VoteResult
    id: int

    # The id of the legislator casting a vote
    legislator_id: int

    # The id of the Vote associated with this cast
    vote_id: int

    # The type of vote cast - 1 for yea and 2 for nay
    vote_type: int