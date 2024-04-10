#Task 1
numbers = [1, 2, 3, 3, 17, 19, 17]
def uniq_numbers(numbers):
    list_numbers = []
    uniq_numbers = set(numbers)

    for el in uniq_numbers:
        list_numbers.append(el)

    return list_numbers

print(uniq_numbers(numbers))    

#Проще конечно так:
uniq_numbers = list(set(numbers))
print(uniq_numbers)

#Task 2
def list_numbers(a, b):
    range(a, b)
    for i in range(a, b):
        print(i)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
list_numbers(a, b)

#Task 3
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def distance(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance
    

point1_x = float(input("point1_x: "))
point1_y = float(input("point1_y: "))
point2_x = float(input("point2_x: "))
point2_y = float(input("point2_x: "))

point1 = Point(point1_x, point1_y)
point2 = Point(point2_x, point2_y)

print(point1.distance(point2))

#Task 4
sortList = ['app', 'circle', 'while', 'elements']
sorted_len = sorted(sortList, key=len)
sorted_len_reverce = sorted(sortList, key=len, reverse=True)
print(sorted_len, sorted_len_reverce)

