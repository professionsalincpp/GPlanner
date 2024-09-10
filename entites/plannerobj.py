from abc import ABC, abstractmethod

class PlannerObject(ABC):
    def __init__(self, id) -> None:
        self.id = id
    
    @abstractmethod
    def save(self) -> str:
        pass
    
    @abstractmethod
    def load(self, data: str) -> None:
        pass

    @abstractmethod
    def draw(canvas: ...) -> None:
        pass

