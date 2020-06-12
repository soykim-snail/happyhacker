# 1. set
set_a = {1, 2, 3}
set_b = {3, 6, 9}

print(set_a - set_b) # 차집합
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

set_c = {1, 1, 1} # {1}
print(set_c)

set_d = set()
print(type(set_d))

# 2. dictionary
dict_a = {}  # 권장되는 방법이다.
print(type(dict_a))
dict_b = dict() # 메모리 소모 큼
print(type(dict_b))

dict_a = {1: 1, 2: 2, 3: 3, 1: 4} # 키가 겹친다. 나중선언값 덮어씌워진다. 
print(dict_a) # {1: 4, 2: 2, 3: 3}

phone_book = {
    '서울': '02',
    '경기': '031'
    }
# dictinary은 key로 접근한다.  
# (그러나, 키밸류쌍의 순서는 보장된다.)  
print(phone_book['서울'])

# print(dir(dict))
# ['__class__', '__contains__', '__delattr__', '__delitem__', 
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', 
# '__len__', '__lt__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
#  '__sizeof__', '__str__', '__subclasshook__',
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
#  'pop', 'popitem', 'setdefault', 'update', 'values']

print(phone_book.keys()) # dict_keys(['서울', '경기'])
print(phone_book.values()) # dict_values(['02', '031']) ---- list 처럼 사용 가능

# print(help(dict))

# dictionary는 집합연산 할 수 없음
# print('차집합', dict_a - dict_b) #타입에러
# print('합집합', dict_a | dict_b) #타입에러
# print('교집합', dict_a & dict_b) #타입에러