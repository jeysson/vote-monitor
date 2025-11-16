from abc import ABC, abstractmethod
from backend.domain.bill import Bill
from typing import List, Optional

"""
It's an interface for BillRepository.
"""
class BillRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Bill]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Bill]:
        pass