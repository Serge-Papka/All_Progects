# C1.9
# Создадим файл rectangle_2.py в отдельной директории в папке
# (назовём её python_practice).
# Выполним импорт класса Rectangle:
from C.practice_C1.rectangle import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)


# вывод площади наших двух прямоугольников
# print(rect_1.get_area())
# print(rect_2.get_area())

# Запустим наш исходный код, чтобы получить результат вычисления
# площади уже двух прямоугольников.

square_1 = Square(5)
square_2 = Square(10)

# print(square_1.get_area_square(),
#       square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

Cir1 = Circle(1)
print(Cir1.get_area_circle())


