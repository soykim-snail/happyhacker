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

- 어플리케이션 만들기

  `$ python manage.py startapp <앱 이름>`

- 환경 세팅 (settings.py)

  ```python
  INSTALLED_APPS = [ ..로칼앱 추가.., ]
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

- 서버 켜기

  `$ python manage.py runserver`  ( 서버 끄기 : `ctrl+c` )

- 브라우저에서 로켓 확인하기

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

콘솔 단축키 : `cntrl + l` (화면 지우기)





# ORM (Object Relational Mapping)

- OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 OOP 프로그래밍 언어간에 호환되지 않는 데이터를 변환하는 프로그래밍 기법

![image](https://user-images.githubusercontent.com/58576911/84608322-deb2dc00-aeec-11ea-82e4-e32a132245a6.png)

## 장점

- SQL을 몰라도 코딩 가능함. 생산성 좋다

## 단점

- 완벽하게 대체는 불가능

---

# Python 클래스

### 클래스

- 클래스란 객체를 표현하기 위한 문법.

### 인스턴스

- 메모리상에 할당된다.
- 고유의 속성(attribute)를 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다. 
- 인스턴스의 행위는 클래스에 정의된 행위에 대한 메서드를 공유함으로써 메모리를 절약할 수 있음

### 속성(attribute)

- 클래스/인스턴스가 가지고 있는 속성(값)

### 메서드(method)

- 클래스/인스턴스가 할 수 있는 행위(함수)

### self

- 인스턴스 자기자신. 
- 메소드 정의할 때 반드시 첫번째 인자는 self

---

### Django Models

1. `CharField()`
   - 길이의 제한이 있는 문자열을 만들 때
   - 
2. `TextField()`
   - 길이의 제한이 없는 문자열을 만들 때

3. `DateTimeField()`

   `models.dateTimeField( … …. )`

   `auto_now_add = True`

   `auto_now = True`

## Model 작성 3단계

1. models.py 작성

   models.py 에 원하는 데이터 스키마를 클래스로 작성한다.	

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터베이스의 최초 생성일
    updated_at = models.DateTimeField(auto_now=True) # 데이터 최신 수정일
```



2. migrations (설계도 작성)

```
$ python manage.py makemigrations
```

​	migrations이 ORM에 의해서 어떻게 sql 문으로 해석되어 동작할 지 미리 확인할 수 있다.

```
python manage.py sqlmigrate <앱이름> <마이그레이션 넘버>
```



3. migrate (DB 작성 및 구축)

```
$ python manage.py migrate
```



python 콘솔 사용하기

- ipython 인스톨 하고 `pip install ipython`, `ipython` 실행하자.

- 장고에서 ipython을 실행하자 ..

  ```python
  python manage.py shell
  ```

  



### objects

- models.py에 작성한 클래스를 불러와서 사용할 때 DB와의 인터페이스 역할을 하는 매니저

## Query Set

- objects 매니저를 사용하여 복수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체 타입
- 단일 객체는 Query (class의 인스턴스로 반환)
- query를 DB에게 보내서 CRUD 한다. 

---

# Django ORM CRUD

## CREATE

```python
# 1
article = Article()
article.title = 'first'
article.content = 'django!
article.save()

# 2
article = Article(title='second', content='django')
article.save()

# 3
Article.objects.create(title='third', contend='django!')
```

## READ

```python
# 모든 객체 조회
Article.objects.all()

# 특정 객체 조회
Article.objects.get(pk=1)

# 특정 조건 객체 가져오기
Article.objects.filter(title='first')
Article.objects.filter(title='first', content='django!')

# 내림차순
Article.objects.order_by('-pk')

# LIKE
Article.objects.filter(title__contains='fi')   
Article.objects.filter(title__startswith='fi')
Article.objects.filter(content__endswith='!')
```

- `.get()`을 사용할 때 해당 객체가 없으면 `DoesNotExist` 에러가 발생하고, 여러 개일 때 `MultipleObjectReturned` 에러가 발생함. ==> 이와 같은 특징 때문에 pk 사용한다.
- 읽어온 결과는 `Article` 객체 또는  `QuerySet` 로 저장된다. 

```shell
# Article 객체
In [8]: Article.objects.get(pk=2)
Out[8]: <Article: Article object (2)>

# QuerySet
In [9]: Article.objects.filter(my_title__startswith="tt", my_content__endswith="d")
Out[9]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```





## UPDATE

```python
article = Article.objects.get(pk=1) # 선택하고
article.title = 'edit title' # 업데이트 한 후
article.save() # 저장
```

## DELETE

```python
article = Article.objects.get(pk=1) # 선택하고
article.delete() # 삭제
```

---

# 관리자 기능 사용하기

계정 또한 데이터이기 때문에 반드시 migrate 작업 후에 관리자 계정을 생성해야 한다.

## admin 작성 순서

1. `python manage.py createsuperuser`
2. `admin.py` 작성

