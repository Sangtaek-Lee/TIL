django - model



sql  : database 다루는 언어

orm : sql 언어를 python으로 감싸 python 문법으로 사용 (java에도 존재)

migrations : model 의 히스토리를 쌓는거

CRUD : Create Read Update Delete (생성, 읽기, 수정, 삭제) 프로그램의 기본적인 기능



- Model
  - 단일한 데이터에 대한 정보를 가짐 (django 데이터 구조)
  - 웹 애플리케이션(장고)의 데이터를 구조화하고 조작(CRUD)하기 위한 도구



스키마 : 설계도, 구조

테이블 : 표

행(레코드)

PK(Primary Key : 기본키) : 중복 불가, 데이터 베이스 관리 및 설정시 주요하게 활용



- ORM

Object Relational Mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터(장고 - sql)를 변환하는 프로그래밍 기술

sql vs nosql 두 구조가 있다.



python manage.py sqlmigrate app.name 0001 # sql로 변환 된 데이터

```
# 마이그레이션 파일 생성 
$ python manage.py makemigrations <app-name> 
# 마이그레이션 적용 
$ python manage.py migrate <app-name> 
# 마이그레이션 적용 현황 
$ python manage.py showmigrations <app-name> 
# 지정 마이그레이션의 SQL 내역 
$ python manage.py sqlmigrate <app-name> <migration-name>
```

DateTimeField auto_now_add 최초 생성 시간, auto_now 조작 시 마다



DB 와 ORM 사이 data를 바로 조작하고 볼 수 있는 환경이 있다.

환경 접속



# Create

$ python manage.py shell

데이터 row 생성

#인스턴스를 만들고 save

article = Article()

article.attribute = "data"

article.save()

#keyword 인잘르 넘기는 방식

article = Article(attribute = "")

article.save()

#create() 이용하는 방법 save 자동

Article.objects.create(attribute="")

# Read

objects.get()  은 반드시 한가지 데이터만 가져옴 2개 이상은 error

objects.filter()

# Update

article.attribute = "data" 로 덮어 쓰면 된다.

# Delete

article = Article.objects.get(id="")  지울 내용 담는다

article.delete()								지운다.







# 관리자

/admin

python manage.py  createsuperuser  로그인 계정 생성





http method 시멘틱한 의미가 있다.

get : 기본값, 서버 리소스를 요청할 때, url에 query string 으로 보낸다.

post : 리소스를 생성,수정,삭제할때, body 안쪽에 data를 숨겨 보낸다.



데이터를 추가할 때 url query로 submit 하면 query 조작, 새로고침으로 계속 데이터가 추가 될 수 있다는 문제가 있다.

csrf 공격 사용자인척 공격하는것

csrf token 을 이용해 토큰 값 비교해 방어

POST 는 CSRF Token 을 항상 사용해야 된다. 

장고는 {% csrf_token %} 태그를 작성해 주면 자동으로 토큰 비교해준다.

settings 의 middleware 에 보면 csrf 가 있다. middleware는 요청시 거쳐가야 되는 중간 장소