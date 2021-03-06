# for 문은 정해진 범위 내 시퀀스 (문자열, 튜플, 리스트 등등)나
# 다른 반복 가능한 객체 (iterable)의 요소들을 순차적으로 실행합니다.

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(100):
    print(i)

result = []
for num in range(1, 31):
    if num % 2: # 나머지가 있는 경우
        result.append(num)
print(result)

result = []
for num in range(1, 31):
    if num % 2 == 0: # 나머지가 0인 경우
        result.append(num)
print(result)

result = []
for num in range(1, 31):
    if num % 2: # 나머지가 있는 경우 패스하라
        pass
    else:
        result.append(num)
print("mytest:", result)

# 인덱스도 출력하는 경우
# enumerate
lunch = ['짜장면', '초밥', '탕수육']
for idx, menu in enumerate(lunch): # 인덱싱 시작값 설정가능
    print(idx, menu)

print(enumerate(lunch))
print(type(enumerate(lunch)))
print(list(enumerate(lunch))) 
print(type(list(enumerate(lunch))[0])) # tuple

print("---str is sequence---")
phrase = "My Run Never Stop!"
for idx, char in enumerate(phrase, 1):
    print(idx, char)

print(phrase[::-1]) # 문자 뒤집기

print("---range is sequence---")
nums = range(10)
for idx, n in enumerate(nums):
    print(idx, n)

print(nums[::-1]) # range 뒤집기  range(9, -1, -1)