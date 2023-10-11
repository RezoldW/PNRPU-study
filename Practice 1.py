<<<<<<< HEAD
from random import randint
import random
numbers = []
numbers_reversed = []
numbers_first = []
numbers_second = []

def firsttask():
    for i in range(20):
            numbers.append(randint(-10, 10))
    print(numbers)
    for i in reversed(numbers): 
        numbers_reversed.append(i)
    print(numbers_reversed)

def secondtask():
    for i in range(20):
            numbers_first.append(randint(-10, 10))
    for i in range(20):
            numbers_second.append(randint(-10, 10))
    print(numbers_first)
    print(numbers_second)
    numbers_complex = []
    for i in range(20):
        if i%2==0:
            numbers_complex.append(numbers_first[i])
        else:
            numbers_complex.append(numbers_second[i])
    print(numbers_complex)

def thirdtask():
    random_list = [random.randint(1, 10) for i in range(10)]
    random_list += [random.uniform(1, 10) for i in range(5)]
    random_list += [random.choice(['one', 'two', 'three']) for i in range(5)]
    print("Исходный список:")
    print(random_list)
    unique_list = list(set(random_list))
    print("Список без дубликатов:")
    print(unique_list)

def fourthtask():
    random_dict = {}
    for i in range(10):
        key = ''.join(random.choice('abcdefghijkl') for i in range(5))
        value = random.randint(1, 10) if random.random() < 0.5 else random.uniform(1, 10)
        random_dict[key] = value
    print("Исходный словарь:")
    print(random_dict)
    unique_tuples = []
    for value in set(random_dict.values()):
        keys = [key for key, val in random_dict.items() if val == value]
        unique_tuples.append((value, keys))
    print("Список кортежей:")
    print(unique_tuples)

def fifthtask():
    dict1 = {str(i): random.randint(1, 10) for i in range(5)}
    dict2 = {str(i): random.randint(1, 10) for i in range(5)}
    print("Первый словарь:", dict1)
    print("Второй словарь:", dict2)
    intersection = set(dict1.values()) & set(dict2.values())
    print("Пересечение множеств значений словарей:", intersection)
    new_dict = {key: value for key, value in dict1.items() if value in intersection}
    print("Новый словарь:", new_dict)

print('\n\n') 
print('Решение первого задания')
firsttask()
print('\n\n') 
print('Решение второго задания')
secondtask()
print('\n\n') 
print('Решение третьего задания')
firsttask()
print('\n\n') 
print('Решение четвертого задания')
fourthtask()
print('\n\n') 
print('Решение пятого задания')
fifthtask()
print('\n\n') 

                
          
    



=======
from random import randint
import random
numbers = []
numbers_reversed = []
numbers_first = []
numbers_second = []

def firsttask():
    for i in range(20):
            numbers.append(randint(-10, 10))
    print(numbers)
    for i in reversed(numbers): 
        numbers_reversed.append(i)
    print(numbers_reversed)

def secondtask():
    for i in range(20):
            numbers_first.append(randint(-10, 10))
    for i in range(20):
            numbers_second.append(randint(-10, 10))
    print(numbers_first)
    print(numbers_second)
    numbers_complex = []
    for i in range(20):
        if i%2==0:
            numbers_complex.append(numbers_first[i])
        else:
            numbers_complex.append(numbers_second[i])
    print(numbers_complex)

def thirdtask():
    random_list = [random.randint(1, 10) for i in range(10)]
    random_list += [random.uniform(1, 10) for i in range(5)]
    random_list += [random.choice(['one', 'two', 'three']) for i in range(5)]
    print("Исходный список:")
    print(random_list)
    unique_list = list(set(random_list))
    print("Список без дубликатов:")
    print(unique_list)

def fourthtask():
    random_dict = {}
    for i in range(10):
        key = ''.join(random.choice('abcdefghijkl') for i in range(5))
        value = random.randint(1, 10) if random.random() < 0.5 else random.uniform(1, 10)
        random_dict[key] = value
    print("Исходный словарь:")
    print(random_dict)
    unique_tuples = []
    for value in set(random_dict.values()):
        keys = [key for key, val in random_dict.items() if val == value]
        unique_tuples.append((value, keys))
    print("Список кортежей:")
    print(unique_tuples)

def fifthtask():
    dict1 = {str(i): random.randint(1, 10) for i in range(5)}
    dict2 = {str(i): random.randint(1, 10) for i in range(5)}
    print("Первый словарь:", dict1)
    print("Второй словарь:", dict2)
    intersection = set(dict1.values()) & set(dict2.values())
    print("Пересечение множеств значений словарей:", intersection)
    new_dict = {key: value for key, value in dict1.items() if value in intersection}
    print("Новый словарь:", new_dict)

print('\n\n') 
print('Решение первого задания')
firsttask()
print('\n\n') 
print('Решение второго задания')
secondtask()
print('\n\n') 
print('Решение третьего задания')
firsttask()
print('\n\n') 
print('Решение четвертого задания')
fourthtask()
print('\n\n') 
print('Решение пятого задания')
fifthtask()
print('\n\n') 

                
          
    



>>>>>>> ceceaa4f42860150f43f5073945cd3e543bf944d
