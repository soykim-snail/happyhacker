

참고자료: https://docs.python.org/ko/3.7/

설치: Python 3.7.6  Windows x86-64 executable (최신 버전은 3.8.x이나 타 라이브러리와 호환성을 위해 3.7x를 설치함)

# 00. data type

숫자형 (int, float, complet)

bool

문자형

### string interpolation

1. %-formatting : `‘Hello %s’ name`
2. .format() : `‘Hello {}’.format(name)`
3. f-string : `f'Hello {name}'`

# 01. operations

- 단축평가
- in 연산자 : 요소가 속해있는지 여부를 확인할 수 있다.

# 02. sequence data

의미: 

- 데이터가 순서대로 나열된 형식이다.
- 데이터에 순서(번호)를 붙여 나열한 것이다.
- (주의!!) 정렬된 것은 아님

종류:

1. 리스트 (list)
2. 튜플 (tuple)
   - 하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
3. range()
   - 리스트나 튜플에 비해 범위의 크기에 무관하게 항상 같은 양의 메모리를 사용한다.
   - (주의!!) range가 반환한 객체는 iterable 이다. 

# 03. slicing

- 파이썬의 슬라이싱은 공간을 분할하는 것으로 이해하자

  [   0,   1,   2,   3,   4,   5   ]

    0—1—-2—3—4-–5—6

- [1:5:3]
- [::-1]  ….. 뒤집기

# 04. set & dictionary

## set

- {1, 2, 3}
- 순서가 없는 자료구조
- 집합의 요소는 unique 하다.
- 요소의 위치나 삽입 순서를 기록하지 않는다.
- 인덱싱, 슬라이싱 또는 기타 시퀀스와 유사한 동작을 지원하지 않는다.
- 수합의 집합연산이 가능하다.
  - `-` (차집합)
  - `|` (합집합)
  - `&` (교집합)
- 만드는 법 : `set()`

## dictionary

- key와 value가 쌍으로 이루어져 있으며, 궁극의 자료구조라고 한다. 
- key 중복이 되어선 안되며, 중복되면 나중 작성된 key 값으로 덮어씌워진다.
- key는 불변한(immutable) 모든 것이 가능하다. (str, int, float, bool, tuple, range)
- value는 list, dict를 포함한 모든 것이 가능하다.
- 만드는 법 : `{}`, `dic()`
- 항상 key로 접근한다. (그러나 키밸류쌍의 순서는 보장된다.)
  - my_dic[‘key’] … 키 없으면 key error
  - my_dic.get(‘key’) … 키 없으면 none
- 메소드: `.keys()`, `.values()`

-----

# 데이터 타입

## 1. 시퀀스 (ordered)

- string
- list (가변)
- tuple
- range



## 2. Unordered

- set (가변)
- dictionary (가변) …. key는 불변

-----

# 05. if statements

```python
x = int(input("숫자를 입력하세요."))
if x < 0:
    print('Negative')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```



# 06. while statments

while 문은 조건식이 참인 경우 반복적으로 코드를 실행한다.

조건식이 False 일 때까지 실행.

종료조건을 반드시 설정해주어야 한다.

# 07. for statments

- list에서 꺼내기

  : 인덱스도 출력하는 경우 시퀀스를 `enumerate`  함수로 감싸서 사용한다.

  - str, range 모두 사용 가능

# 08. for with dictionary

- dictionary에서 꺼내기
  - `.keys()`, `.values()`, `.items()`  사용한다. 

# 09. list comprehension

- 시퀀스의 요소들 전부 또는 일부를 처리하고, 그 결과를 리스트로 돌려주는 간결한 방법
- 즉, 반복을 통해 리스트에 어떠한 것을 담는 경우 한줄로 줄여쓰는 것
- (주의!!) 단순히 반복문을 한 줄로 작성하는 것이 아님
- 특징

  1. 간결함

  2. 성능 (반드시 그런 것은 아님)

  3. 표현력 (*Pythonic*)
- 리스트컴프리헨션을 남용하지 말자.
- 조건표현식

```python
[x**2 for x in range(10)]
[x**2 for x in range(100) if x % 4 == 0]
[x + 7 if x >= 50 else x + 5 for x in range(100)]
```

# 10. module Random

모듈 임포트 방법 : 

- `import <모듈이름>`
- `from <패키지이름> import <모듈이름>`

```python
import random
random.choice(['사과', '바나나', '귤', '사과'])
random.sample(range(100), 3)
```

유용한 메소드 : `random.choice(<sequence>)`, `random.sample(<sequence>, k)`

# 11. module requests

정적크롤링 : requests 패키지

# 12. my mask

requests 패키지를 사용하여 

https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json  데이터 받아 오기 실습

# 13. function

함수 정의 방법 (주의!  리턴 값이 없을 수도 있음)

```python
def 함수이름(...):
    ... ...
    return ..........
```

함수 호출 방법

```python
함수이름()
```

# 14. my function

외부 모듈에서 임포트 해 온 함수를 사용할 수 있다.

```python
from public import public_mask  # 인스톨
public_mask.mask('서울특별시 강남구 역삼동')
```




