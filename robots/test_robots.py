#coding:utf8
import unittest
from .creature import Spider, Creature



class TestChemicalProperties: 

  # Reactions between the reagents
  # TODO: check test before first start, and do in after creating source of classes Creature: and Spider:
  def test_add_connection(self):
    self.assertEqual(Creature(Spider(chemical=[
      (
        [(13, 13), (13, 13)], 
       [(17, 17), (17, 17), (17, 17)]
      ), 
    ]), perimeter=(100,100,100)), 
                    [
                      (
                       (13, 17), (13, 17), (13, 17)
                      ), 
                      (
                       (13, 17), (13, 17), (13, 17)
                      )
                    ]
      )

import unittest
from my_module import add_numbers, is_even

class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        # Проверка сложения положительных чисел
        self.assertEqual(add_numbers(2, 3), 5)
        # Проверка сложения с отрицательным числом
        self.assertEqual(add_numbers(-1, 1), 0)
        # Проверка сложения нулей
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        # Проверка для чётного числа
        self.assertTrue(is_even(4))
        # Проверка для нечётного числа
        self.assertFalse(is_even(5))
        # Проверка для нуля (ноль считается чётным)
        self.assertTrue(is_even(0))

# Эта конструкция позволяет запускать тесты из командной строки
if __name__ == '__main__':
    unittest.main()
class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        # Проверка сложения положительных чисел
        self.assertEqual(add_numbers(2, 3), 5)
        # Проверка сложения с отрицательным числом
        self.assertEqual(add_numbers(-1, 1), 0)
        # Проверка сложения нулей
        self.assertEqual(add_numbers(0, 0), 0)

    def test_is_even(self):
        # Проверка для чётного числа
        self.assertTrue(is_even(4))
        # Проверка для нечётного числа
        self.assertFalse(is_even(5))
        # Проверка для нуля (ноль считается чётным)
        self.assertTrue(is_even(0))

# Эта конструкция позволяет запускать тесты из командной строки
if __name__ == '__main__':
    unittest.main()
