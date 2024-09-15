#zavdani'e 5 prime number degenerator + tests
import math
import unittest

degug_flag = False
do_spam = False

def is_prime(number):
    if degug_flag: print(number)
    if number <= 1:
        if do_spam:print("Число не может является простым тк <= 1")
        return False
    for i in range (2, int(math.sqrt(number))+1):
        if degug_flag: print("Перебор делителей для ", number, " Делитель: ", i)
        if number % i == 0:
            return False
    return True

def find_nearest_prime(number):
    if is_prime(number): 
        if do_spam:print(f'Число {number} простое.') 
        return number

    lower = number - 1
    upper = number + 1

    while True:
        if is_prime(lower): 
            if do_spam:print(f"Простое число рядом с {number} найдено: {lower}")
            return lower
        if is_prime(upper): 
            if do_spam:print(f"Простое число рядом с {number} найдено: {upper}")
            return upper
        lower -= 1
        if degug_flag: print(f"new lower number: {lower}")
        upper += 1
        if degug_flag: print(f"new upper number: {upper}")

class TestPrimeFunctions(unittest.TestCase):

    def test_nearest_prime_same_number(self):
        self.assertEqual(find_nearest_prime(7), 7)
        self.assertEqual(find_nearest_prime(11), 11)
    
    def test_nearest_prime_lower(self):
        self.assertEqual(find_nearest_prime(9), 7) 
    
    def test_nearest_prime_upper(self):
        self.assertEqual(find_nearest_prime(10), 11)
    
    def test_nearest_prime_edge_case(self):
        self.assertEqual(find_nearest_prime(1), 2)  
        self.assertEqual(find_nearest_prime(2), 2) 
        self.assertEqual(find_nearest_prime(3), 3) 

def checkbox(answer):
    if answer == "T":
        unittest.main()
        return
    else:
        print(find_nearest_prime(int(input("Напишите число: "))))
        return


print(checkbox(str(input("Любая клавиша - Генератор простого числа, T - Запустить тест: "))))







