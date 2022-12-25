from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def is_inside(x, y) -> bool:
        pass


class Square(Shape):
    def is_inside(x: float, y: float) -> bool:
        inside = True
        if x < 0 or x > 1:
            inside = False
        if y < 0 or y > 1:
            inside = False

        return inside
