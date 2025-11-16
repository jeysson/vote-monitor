from abc import ABC, abstractmethod
from backend.domain.vote_result import VoteResult
from typing import List, Optional

"""
It's an interface for VoteResultRepository.
"""
class VoteResultRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[VoteResult]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[VoteResult]:
        pass

    @abstractmethod
    def get_by_legislator_id(self, legislator_id: int) -> List[VoteResult]:
        pass

    @abstractmethod
    def get_by_vote_id(self, vote_id: int) -> List[VoteResult]:
        pass