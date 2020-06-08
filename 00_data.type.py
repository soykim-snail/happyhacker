print('Hello, World')

number = 10
string = '문자열'
bools = True
print(number, string, bools)

# 수자형 (int, float, complet)
a = 3
print(type(a))

# bool
print(type(False))
# 0, 0.0, (), [], {}, '', None 는 -> False 로 처리

# 문자형
greeting = 'hi'
name = 'harry'
print(greeting, name)
print(type(name))

# 입력값 ..... 문자형으로 인식
# age = input() 
# print(age)
# print(type(age))

print("""
개행문자 없이
여러줄을
그대로 출력 가능합니다.
""")

print(3*'hey'+' yo!')

# string interpolation
name = 'kim'
# 1. %-formatting  .... 버전 2.+
print('Hello, %s' % name)
# 2. .format()
print('Hello, {}' .format(name))
# 3. f-string (Literal String Interpolation) .... 버전 3.6+
print(f'Hello, {name}')

pi = 3.14192
print(f'원주율은 {pi:.4}. 반지름이 2일 때 원의 넓이는 {2*pi*2}')