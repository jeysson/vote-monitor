from abc import ABC, abstractmethod
from backend.domain.vote import Vote
from typing import List, Optional

"""
It's an interface for VoteRepository.
"""
class VoteRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Vote]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Vote]:
        pass

    @abstractmethod
    def get_by_bill_id(self, bill_id: int) -> List[Vote]:
        pass