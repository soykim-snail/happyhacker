my_list = []

for x in range(10):
    my_list.append(x ** 2)
print(my_list)

# list comprehension 사용
my_newlist = [x**2 for x in range(10)]
my_newlist2 = list(x**2 for x in range(10))
print(my_newlist)
print(my_newlist2)

# list comprehension with if statements
numbers = list(range(10, 100, 10))
print(numbers)

my_numbers_1 = []
for number in numbers:
    if number % 4 == 0:
        my_numbers_1.append(number)
print(my_numbers_1)

my_numbers_2 = [number for number in numbers if number % 4 == 0]
print(my_numbers_2)


my_numbers_3 = []
for number in numbers:
    if number >= 50:
        my_numbers_3.append(number + 7)
    else:
        my_numbers_3.append(number + 5)
print(my_numbers_3)

# 조건 표현식
# true_vale <if> 조건식 <else> false_value
my_numbers_4 = [number + 7 if number >= 50 else number + 5 for number in numbers]
print(my_numbers_4)

# 중첩된 for statement
gugu = []
for a in range(2, 10):
    for b in range(1, 10):
        gugu.append(a * b)
print(gugu)

gugu_2 = [a * b for a in range(2, 10) for b in range(1, 10)]
print(gugu_2)