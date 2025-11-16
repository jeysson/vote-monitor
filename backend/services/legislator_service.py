from typing import List
from backend.domain.legislator import Legislator
from backend.interfaces.legislator_repository import LegislatorRepository

class LegislatorService:
    def __init__(self, repository: LegislatorRepository):
        self.repository = repository

    def get_all(self) -> List[Legislator]:
        return self.repository.get_all()
