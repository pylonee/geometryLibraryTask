# Geometry Shapes Areas and Other Library

import math
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T', bound='Shape')

class Shape(ABC, Generic[T]):
    # Базовый класс для фигур
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @classmethod
    def unknown_Shape(cls, data: dict) -> T:

        # метод для создания фигуры из списка.
        # можно расширять новыми фиурами
        # Можно создавать фигуры без знания типа в compile-time.

        shape_type = data.get('type')
        if shape_type == 'circle':
            return Circle(data['radius'])
        elif shape_type == 'triangle':
            return Triangle(data['side_a'], data['side_b'], data['side_c'])
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


class Circle(Shape):
    # Класс круг
    
    def __init__(self, radius: float):

        # Инициализирует круг с заданным радиусом.

        # radius: Радиус круга (должен быть положительным)
        # ValueError: Если радиус круга не положительный

        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self) -> float:
        # Площадь круга по формуле Pi*r^2
        return math.pi * self.radius ** 2


class Triangle(Shape):
    # Класс треугольник
    
    def __init__(self, side_a: float, side_b: float, side_c: float):

        # Инициализирует треугольник с тремя сторонами.
        
        # side_a,side_b, side_c: Длины трех сторон
        # ValueError: Если стороны не образуют допустимый треугольник

        sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if not self._is_valid_triangle(sides):
            raise ValueError("Invalid triangle sides")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self) -> float:

        # Вычисляет площадь треугольника по формуле Герона: sqrt(p*(p-a)*(p-b)*(p-c))
        # p - полупериметр: p = (a+b+c)/2

        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(
            p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)
        )
    
    def is_right(self) -> bool:

        # Проверка, является ли треугольник прямоугольным: a^2 + b^2 = c^2,
        # используя теорему Пифагора
        
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return(
            sides[0]**2 + sides[1]**2 == sides[2]**2
        )
    
    @staticmethod
    def _is_valid_triangle(sides: list[float]) -> bool:
        # Проверяет, могут ли стороны образовать треугольник
        return (
            sides[0] + sides[1] > sides[2] and
            sides[0] + sides[2] > sides[1] and
            sides[1] + sides[2] > sides[0]
        )


# Можно расширять новыми фигурами
# Создать класс новой фигуры с __init__(self, ...) с проверкой на существование фигуры
# Обязательна функцию area(находждение площади), потому что наследуемся от базового Shape, в котором есть абстрактный метод area
# Написать дополнительные проверки / методы для фигуры
# 
# В базовый класс Shape в метод unknown_Shape расширить список фигур



def calculate_area(shape: Shape) -> float:
    # Вычисляет площадь фигуры без знания её конкретного типа в compile-time.
    # shape: Объект фигуры, унаследованный от Shape

    return shape.area()