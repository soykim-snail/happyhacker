# 논리 연산자
print('--- and ---')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('--- or ---')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('--- not ---')
print(not True)
print(not 0)

# 단축평가
# 첫번째 값이 확실할 때, 두번째 값은 확인하지 않음
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
print('--- 단축평가 ---')
vowels = 'aeiou'
print(('a' and 'b') in vowels)  # b in vowels?
print(('b' and 'a') in vowels)  # a in vowels?
print('a' and 'b')  # 첫값 True 이므로 둘째값도 확인함

# and는 둘 다 True 일 졍우만 True 이기 때문에
# 첫번째 값이 True라도 두번째 갓을 확인해야 한다.
print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0 (왼쪽 0)

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0 (오른쪽 0)

# Containment Test
# in 연산자  : 요소가 속해있는지 여부를 확인할 수 있다.
print('--- in ---')
print('a' in 'apple')  # True
print(1 in [1, 2, 3]) # True  # 리스트 (= 배열)