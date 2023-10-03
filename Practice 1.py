from random import randint
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


            
