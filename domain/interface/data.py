from abc import ABC, abstractmethod
from typing import List, Optional

class DataInterface(ABC):

    @abstractmethod
    def save(self, data: dict) -> Optional[dict]:
        pass

    @abstractmethod
    def get(self, id: int) -> Optional[dict]:
        pass

    @abstractmethod
    def filter(self, data: dict) -> Optional[List[dict]]:
        pass
      
    @abstractmethod
    def update(self, data: dict) -> bool:
        pass