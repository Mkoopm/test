from abc import ABC, abstractmethod
import numpy as np


class Shape(ABC):
    @abstractmethod
    def is_inside(x, y) -> bool:
        pass


class AreaCalculator(ABC):
    shape: Shape

    @abstractmethod
    def calc_area() -> float:
        pass


class Square(Shape):
    def __init__(self) -> None:
        pass

    def is_inside(self, x: float, y: float) -> bool:
        inside = True
        if x < 0 or x > 0.5:
            inside = False
        if y < 0 or y > 0.5:
            inside = False

        return inside


class MonteCarloAreaCalculator:
    def __init__(self, shape: Shape) -> None:
        self.shape = shape

    def calc_area(self) -> float:
        n_points = 10000
        x_arr = np.random.rand(n_points)
        y_arr = np.random.rand(n_points)
        print(f"length = {len(x_arr)}")
        n_inside = 0
        n_outside = 0
        for x, y in zip(x_arr, y_arr):
            if self.shape.is_inside(x, y):
                n_inside += 1
            else:
                n_outside += 1

        area = n_inside / n_points
        print(f"area = {area}")
        return area
