# 1. 리스트 (list)
my_list1 = [10, '문자열', True]
print(my_list1)
print(type(my_list1))
print(my_list1[1])

# 2. 튜플 (tuple)
# 수정 불가능 (불변, immutable) --- 접근 불가, 조회만 가능
# 직접 만들 일은 별로 없다. 파이썬 내부에서 사용됨.
my_tuple1 = (1, 2)
print(my_tuple1)
print(type(my_tuple1))

# 파이썬은 어떻게 내부적으로 튜플 사용하나?
my_tuple2 = 1, 2
print(my_tuple2)
print(type(my_tuple2))

x, y = 1, 2
print(x) # 1
print(y) # 2

x, y = y, x
print(x) # 2
print(y) # 1

# 하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
single_tuple = ('hello',)
print(type(single_tuple))

# 3. range()
# range는 숫자의 시퀀스를 나타내기 위해 사용
print(type(range(1)))
print(list(range(10)))
