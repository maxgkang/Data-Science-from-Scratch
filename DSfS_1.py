# sets, import, class, assert, comprehension, generator, OOP, arg/kwarg, pythonic, dunder, enumerate, help, filter, sorted, zip, open, broadcasting
# collections - Counter and defaultdict , type hinting, asyncio, @property, @staticmethod, 


# sets: set = {1, 2, 3} , set.add(4), 4 in set -> True
# a = [1, 2, 3, 1, 2, 4] , a = set(a), then a = {1, 2, 3, 4}
# sorting: sorted() and sort() , can use reverse = True
# List comprehensions List = [x for in range(5) if x % 2 == 0] , {x: x**2 for x in range(5)} -> 매우 유용함! 

# def smallest(xs):
#     return xs
# assert smallest([10, 3, 4]) == 3

# assert vs raise: assert is activated when it is False, but raise is always activated 

# do if __name__ == '__main__' from file_A import function_A /// But if I have some down right codes in A I do not want in my file_B, 
# place those codes unwanted to print again in file_B under if __name__ == '__main__'
# do if __name__ == '__main__' for file_B's want to print out things too for things meant to be run



def greet() -> None:
    print("Hello")

def bye() -> None:
    print("Bye")

def main() -> None:
    greet()
    bye()

if __name__ == '__main__':
    main()

# This is more readable


class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, amount):
        self.health -= amount

class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed) # 위에 쓴 세 줄을 반복해서 작성 안 해도 됨
        self.toughness_modifier = 0.90 

    def take_damage(self, amount): # 함수 재정의
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount) # 윗 공식 그대로 쓰나, input을 달리함

# 관찰 결과, super()을 이용하면 self를 안 적어도 됨

warrior = Warrior(100, 50, 10)
print(f'Initial health: {warrior.health}')
warrior.take_damage(40)
print(f'Health after damage: {warrior.health}')

# 리스트는 숫자 10억개의 리스트를 만든다면 컴퓨터가 버거워한다

import sys 
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sys.getsizeof(x)) # 차지하는 저장공간 더 큼
print(sys.getsizeof(range(1,11))) # tierator의 한 종류, 즉 모든걸 저장하지 않는다

y = map(lambda i: i ** 2, x)
# print(y) # map object라 뜸. It isn't storing all the values like list

# print(list(y)) # 리스트를 출력해주는데 저장하는 것은 아니다. 출력과 메모리에 저장하는 것을 엄연히 구분해야한다

# print(sys.getsizeof(list(y)))
# print(sys.getsizeof(y))

print(next(y))
print(next(y))
print(next(y))
print(next(y)) # 16까지 

print("For loop starts")

for i in y:
    print(i) # 25부터 100 


alpha = range(1, 11)
print(next(iter(alpha)))

# generator: when the yield keyword is hit it pauses the execution of the function and reutrns this values whatever's iterating through the generator object

# yield 

def gen():
    yield 1
    print("Pause 1")
    yield 2
    print("Pause 2")
    yield 3
    print("Pause 3")
    yield 4

beta = gen()
print(next(beta)) # yield 1 hits, we pause the execution of the function, print beta
print(next(beta))
print(next(beta))

# usage: say you are finding for a word in a big file. you can read all of them and find the word, but using generators, you can 
# read one line -> pause , see if this has the word, if not, go to the second line -> pause, see if this has the word, and continue
# the previous line is not saved nor the next line is saved up front, so it really saves a lot of memory


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

gamma = (i for i in range(1, 11)) # you can create a generator like this too
print(gamma)
print(next(gamma))
print(next(gamma))
print(next(gamma))


# dunder 

class InventoryItem:
    """A class to demonstrate operator overloading for inventory management."""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"

    # Arithmetic Operators
    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError("Cannot add items of different types.")

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError("Cannot subtract more than the available quantity.")
        raise ValueError("Cannot subtract items of different types.")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
             return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError("Multiplication factor must be a number.")

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor))
        raise ValueError("Division factor must be a non-zero number.")
    
    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False

    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("Cannot compare items of different types.")

    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError("Cannot compare items of different types.")
    
item1 = InventoryItem("Apple", 50)
item2 = InventoryItem("Apple", 30)

result_add = item1 + item2
print(result_add)  # 출력: InventoryItem(name='Apple', quantity=80)

print(item1 > item2) # 출력: True
print(item1 == InventoryItem("Apple", 50)) # Output: True


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # __str__ is meant for user-friendly output
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    # __repr__ is meant for a more detailed, unambiguous output
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

# Create an instance of the Car class
my_car = Car('Toyota', 'Corolla', 2021)

# Example usage
print(str(my_car))   # User-friendly output: 2021 Toyota Corolla
print(repr(my_car))  # Developer-friendly output: Car(make='Toyota', model='Corolla', year=2021)


# 정규 표현식 (Regular Expressions)

# 초강력 검색 & 바꾸기(Find & Replace) 도구
#일반적인 Ctrl+F 검색으로는 찾기 힘든 복잡한 패턴을 찾을 때 사용

# .	모든 문자	a.c	abc, aTc, a@c (모두 매칭)
# ^	시작	   ^Hi	문장이 Hi로 시작해야 함
# $	끝	   end$	문장이 end로 끝나야 함
# []	문자 집합	[abc]	a, b, c 중 하나
# [^]	부정	[^0-9]	숫자가 아닌 것
# `	`	또는 (OR)	`a

# *: 0개 이상 (없어도 됨)

# +: 1개 이상 (최소 1개는 있어야 함)

# ?: 0개 또는 1개 (있거나 없거나)

# {n}: 정확히 n번 반복

# {n, m}: n번부터 m번까지 반복

# \d: 숫자 (Digit) [0-9]와 같음

# \w: 문자+숫자 (Word) [a-zA-Z0-9_]와 같음

# \s: 공백 (Space) 스페이스바, 탭 등

import re

text = "제 번호는 010-1234-5678입니다. 집 전화는 02-987-6543이에요."

# 패턴: 숫자-숫자-숫자 형태
pattern = r"\d{2,3}-\d{3,4}-\d{4}"

# search: 첫 번째로 찾는 패턴 하나만 반환
result = re.search(pattern, text)
print(result.group())  # 출력: 010-1234-5678

# findall: 패턴에 맞는 모든 것을 리스트로 반환
results = re.findall(pattern, text)
print(results)  # 출력: ['010-1234-5678', '02-987-6543']



# help

help(print) # <-- 안에 함수 넣으면, 그 함수가 어떤건지 터미널에서 자세히 알려줌

# map

strings = ["my", "world", "apple", "pear"]

# map 함수를 사용하여 리스트의 각 요소에 len 함수를 적용
lengths = map(len, strings)

# 결과를 리스트로 변환하여 출력
print(list(lengths))

# map(lambda x: x + "r", strings) 이런것도 된다
# 근데 이거는 클래스가 map이라서 다른 종류를 원하면 번경해줘야한다



# filter

def longer_than_4(string):
    return len(string) > 4

strings = ["my", "world", "apple", "pear"]
filtered = filter(longer_than_4, strings)
print(list(filtered))


# sum
numbers = {1, 2, 4, 5}
print(sum(numbers, start=10))


# sorted

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20},
]

sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)

print(sorted_people)


# enumerate

tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheet"]

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")


#%%
# zip
# 여러 리스트의 요소를 하나씩 짝을 지어 튜플 형태로 묶어줍니다.

names = ["Alice", "Bob", "Charlie", "David", "Tim"]
ages = [30, 25, 35, 20]
gender = ["Female", "Male", "Male"]

combined = list(zip(names, ages, gender))
print(combined)

for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender}")

pairs = [('a', 1), ('b', 2)]
letters, numbers = zip(*pairs)
print(letters) # -> ('a', 'b') 생성
print(numbers) # -> (1, 2) 생성


#%%

# open
file = open("test.txt", "w")
file.write("hello world\nMy name is GT")
file.close()
# 생성됨

with open("test.txt", "a") as file:
    file.write("Appended")
#%%

# args and kwargs

def printer(a, b, *args):
    print(a, b, args)

printer('a', 1, 2, 3) # -> a 1 (2,3) 출력함

# args는 튜플 만들기용

# kwargs는 항상 맨 마지막에 있어야 함

def printer_1(a, b, *args, values = [1,2,3], **kwargs):
    print(a, b, values, args, kwargs)

printer_1('a', 1, 2, 3, key = 5, value = 7, values = [1, 2, 3])
# a 1 [1, 2, 3] (2, 3) {'key': 5, 'value': 7} 출력됨

