from abc import ABC, abstractmethod
from backend.domain.legislator import Legislator
from typing import List, Optional

"""
It's an interface for LegislatorRepository.
"""
class LegislatorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Legislator]:
        pass
    
    @abstractmethod
    def get_by_id(self, legislator_id: int) -> Optional[Legislator]:
        pass