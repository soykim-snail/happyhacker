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

# 11. module lotto

정적크롤링 : requests 패키지

# 12. my mask

# 13. function

# 14. my function



-----



# Django

version 2.1.15

### 사용방법

- Django 패키지 인스톨

  `$ pip install django==2.1.15`

- 프로젝트 만들기

  `$ django-admin startproject <프로젝트 이름>`

- 서버 켜기

  `$ python manage.py runserver`

- 서버 끄기

  `ctrl+c`

- 어플리케이션 만들기

  `$ python manage.py startapp <앱 이름>`

- 환경 세팅 (settings.py)

  ```python
  INSTALLED_APPS = [ ..로칼앱 추가.., ]
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

- MTV 패턴에 따른 코딩하기
  1. urls.py 작성
  2. views.py 작성
  3. templates 작성

##### 장고 특징:

trailing comma를 허용한다.

### style convention

\# django import style guides

\# 1. standard library

\# 2. 3rd party library

\# 3. django

\# 4. local django

### jango template language

- variable routing

##### 실습: 사용자의 입력값을 그대로 돌려주는 사이트를 만들어 보자

2개의 view가 필요함

1. throw : 사용자로부터 입력을 받아 서버로 보내는 view
2. catch : 입력받은 값을 보여주는 view

# http request method

1. GET
   - HTTP method 중 GET 요청은 서버로부터 정보를 조회하는데 사용됩니다.
   - 서버의 데이터나 상태를 변경시키지 않기 때문에 단순 조회(html)할 때 사용한다.
   - 데이터를 전송할 때 http body가 아니라 쿼리스트링을 통해 전송된다. 

#### form에서 중요한 것

1. 데이터를 어디로 보낼지 => action
2. 어떤 방식으로 보낼지 => method
3. 어떤 데이터를 보낼지 => input type
4. 데이터의 이름은 어떻게 붙일지 => name
5. 제출 => submit

#### Django Template Language (DTL)

- variable 사용 : `{{ variable }}`

- 반복문, 조건문, 반복조건, 필터 등등

  ```django
  {% for ... in ... %} 
  {% empty %}
  {% endfor %}
  ```
  


### 프로젝트 만들기 (FIRSTAPP)

#### 관리를 위해서 다음을 적용

1. URL 로직 분리
   - 두번째 app을 생성할 때….. 하나의 urls.py에서 모든 문서 path를 관리하기 어려워짐.
   - 프로젝트의 urls를 각 앱으로 분리하자.
   - 기존 url 이 바뀌어버려서 지금까지 작업한 모든 url을 바꿔줘야 함
   - 그건 어려우니 그냥 url에 이름을 붙이자.
2. URL Name : 
   - `{% urls “<url 이름>” %}`
   - 그런데,,, 두개의 앱에서 url 이름이 같다면?
   - 어떤 앱의 url 이름인지 app_name을 설정하자.

3. URL Namespace : 

   `{% urls "app-name:view-name" v1 v2 %}`

4. Django Namespace : 

   장고는 templates를 한곳에 모아두므로 템플릿 파일명이 곂치면 우선순위에 따라 인식한다. 그래서 templates/<앱이름>으로 강제로 경로를 추가한다.

   INSTALLS_APP 에 등록한 순서대로 인식

   > app_name/
   >
   > ​	templates/
   >
   > ​		**app_name/**
   >
   > ​			index.html
   >
   > ​			hello.html

5. Django Template Inheritance 적용:

   - 템플릿의 재사용성을 위해 상속을 사용했다.

     프로젝트에 기본 html을 만들고, 나머지는 이것을 상속한다.

     ```django
     {% extents 'base.html' %}
     {% block <블록이름> %}내용 오버라이드{% endblock %}
     ```

     그런데,,

   장고는 기본적으로 template을 app-name/templates 에서 찾는다.  setting에 추가하여 firstapps/templates도 찾을 수 있게 하자.

   ```django
   TEMPLATES = ... 생략 ...   
           'DIRS': [os.path.join(BASE_DIR, 'firstapp', 'templates')],
   ```

6. static

   장고는 기본적으로 static을 app-name/static 에서 찾는다. setting에 추가하여 firstapps/static도 찾을 수 있게 하자.

   (사용방법은 공식문서를 사용하자.) https://docs.djangoproject.com/en/2.1/howto/static-files/ 

   ```django
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'firstapp', 'static'),
   ]
   ```

   





## VScode, markdown 꿀팁

polar code로 사진찍기, github issue에 사진 저장하고 url 받기

단축키들 : `alt + 화살표` , `cntrl + l`

