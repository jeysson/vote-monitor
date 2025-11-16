from typing import List, Optional
from backend.entities.legislator import Legislator
from backend.repositories.legislator_repository import LegislatorRepository

class LegislatorService:
    def __init__(self, repository: LegislatorRepository):
        self.repository = repository

    def get_all(self) -> List[Legislator]:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Optional[Legislator]:
        return self.repository.get_by_id(id)