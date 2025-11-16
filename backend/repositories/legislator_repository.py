from abc import ABC, abstractmethod
from backend.entities.legislator import Legislator
from typing import List, Optional

"""
It's an interface for LegislatorRepository.
"""
class LegislatorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Legislator]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, legislator_id: int) -> Optional[Legislator]:
        raise NotImplementedError