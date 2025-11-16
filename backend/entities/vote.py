from dataclasses import dataclass

@dataclass
class Vote:
    # The id of the Vote
    id: int

    # The id of the bill that this vote is associated with
    bill_id: str