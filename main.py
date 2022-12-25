from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def is_inside(x,y) -> bool:
        pass