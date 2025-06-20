from GeometryCalc import Shape, Circle, Triangle, calculate_area

def main():
    print("----------------------------------")
    # Создаем фигуры вручную
    circle = Circle(5)
    print(f"Площадь круга: {circle.area():.2f}")
    
    triangle = Triangle(3, 4, 5)
    print(f"Площадь треугольника: {triangle.area():.2f}")
    print(f"Это правильный треугольник: {triangle.is_right()}")
    
    # Создаем фигуры из списка
    shapes_data = [
        {"type": "circle", "radius": 2},
        {"type": "triangle", "side_a": 3, "side_b": 4, "side_c": 5}
    ]
    
    for shape_data in shapes_data:
        shape = Shape.unknown_Shape(shape_data)
        print(f"Площадь {shape_data['type']}: {calculate_area(shape):.2f}")

    print("----------------------------------")



import unittest
import math

class TestGeometryLibrary(unittest.TestCase):
    
    # -------------------------      Тестирование кругов
    def test_circle_area(self):
        # Площадь кругов
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi)
        
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), math.pi * 2.5**2)
    
    def test_circle_validation(self):
        # Создание не существующих кругов (проверка возникновения исключений)
        with self.assertRaises(ValueError):
            Circle(-1)  # Отрицательный радиус
        with self.assertRaises(ValueError):
            Circle(0)   # Нулевой радиус
    

    # -------------------------      Тестирование треугольников
    def test_triangle_area(self):
        # Площадь треугольников
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
        
        triangle = Triangle(5, 5, 5)
        self.assertAlmostEqual(triangle.area(), 10.825317547305483)
    
    def test_triangle_validation(self):
        # Создание несуществующих треугольников (проверка возникновения исключений)
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Несуществующий треугольник
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)  # Отрицательная сторона
        with self.assertRaises(ValueError):
            Triangle(0, 1, 1)   # Нулевая сторона
    
    def test_right_triangle(self):
        # Проверка правильных треугольников
        self.assertTrue(Triangle(3, 4, 5).is_right())   # Правильный треугольник
        self.assertTrue(Triangle(5, 12, 13).is_right()) # Правильный треугольник
        self.assertFalse(Triangle(5, 5, 5).is_right())  # Неправильный треугольник

    
    # -------------------------      Тестирование фигур из списка
    def test_unknown_Shape(self):
        # Фигуры из списка

        # Круг
        circle = Shape.unknown_Shape({"type": "circle", "radius": 10})
        self.assertIsInstance(circle, Circle)   # Проверка типа
        self.assertEqual(circle.radius, 10)     # Проверка равенства
        
        # Треугольник
        triangle = Shape.unknown_Shape({
            "type": "triangle",
            "side_a": 3,
            "side_b": 4,
            "side_c": 5
        })
        self.assertIsInstance(triangle, Triangle)   # Проверка типа
        self.assertEqual(triangle.side_a, 3)        # Проверка равенства стороны

    
    def test_calculate_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(calculate_area(circle), math.pi * 4)
        
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)


if __name__ == "__main__":
    main()
    unittest.main()
