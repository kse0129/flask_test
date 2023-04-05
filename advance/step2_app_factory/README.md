## 애플리케이션 팩토리

엔트리 위치 조정, 코드 조정
```python
app = Flask(__name__)
```
- 현재 위의 코드는 전역변수로 존재
- 프로젝트 규모가 커지면, 순환 참조를 할 확률이 큼
- Flask 객체는 애플리케이션 팩토리라는 형태로 사용 권장

## 방법

플라스크 객체를 생성하는 코드를 특정 패키지 밑에 위치 후 `__init__.py`로 파일 이름 변경
```
service
L __init__.py
```
최종 실행 명령
```
flask --app service --debug run
```

## 블루프린트

url과 함수의 매핑(라우트)을 관리하는 도구

## 부트스트랩

부트스트랩을 적용하여 페이지를 구성한다. flask-bootstrap은 2017년 이후로 업데이트되고 있지 않다.

1. 부트스트랩 [다운로드](https://getbootstrap.kr/docs/5.2/getting-started/download/)

2. 압축 해제 후 static 폴더에 bootstrap.min.css, bootstrap.min.js 이동

다양한 UI 형태를 [예시](https://getbootstrap.kr/docs/5.2/examples/)로 제공하고 있다.

## Flask-WTF

입력폼 유효성 검사 및 비정상적인 루트로 접근시 처리

웹 프로그램에서 폼(form)은 사용자에게 입력 양식을 편리하게 제공한다. form 모듈을 활용하여 데이터 필수 입력 여부, 길이, 형식, 유효성 등을 제어할 수 있다.
```
pip install flask-wtf
```
### 구성

- SECRET_KEY
- CSRF(Cross Site Request Forgery)라는 웹 사이트 취약점 공격(사용자의 요청을 위조하여 웹 사이트를 공격하는 기법)을 방지할 때 사용
    - 웹 페이지를 내려줄 때 CSRF 토큰을 삽입해서 그 값이 요청을 타고 들어오도록 처리한다. 이 값이 요청에 존재하고 값이 유효하다면 정상적인 루트로 진입했다고 인지한다.
    ```html
    <input type='hidden' name='' value=''>
    ```
    SECRET_KEY 값을 기반으로 해싱해서 토큰을 생성한다. 따라서 웹 상에서 가장 잘 지켜야할 정보는 SECRET_KEY를 잘 관리 해야한다.

### 방식

1. OS 레벨에서 설정
2. 파이썬 객체로 설정 (O)
3. 환경변수 파일로 설정
    - 플라스크 객체가 로드하면서 세팅 (O)
    - 플라스크를 가동하면서 세팅
    - 키값, DB 연결값 등

### 실습

- 환경설정(변수)를 세팅해서 SECRET_KEY를 관리
- 질문폼 페이지 생성
```
url: ~/main/question, get
html: question.html

base.html을 상속받아서 내부는 div로만 감싸둔다.
````

## JWT

### 설치
```
pip install PyJWT bcrypt 
```
### 개요

JWT(JSON Web Tokens)는 토큰 기반 인증 방식이다. 세션에 고객 정보를 담아서 보관하지 않고, 고객의 필요한 정보를 토큰에 저장해서 클라이언트가 보관(방식에 따라서는 서버 측에도 DB보관), 이를 증명서로 활용한다.
요청이 왔을 때 권한이 있는지 점검

### 구성

- header(헤더): jwt의 토큰 유형, 사용하는 해시 알고리즘 정보(RSA, SHA256, ...)
- payload(정보): 저장할 정보(클라이언트 정보, 메타데이터, ...)
- signature(서명): 헤더에서 지정한 알고리즘과 플라스크의 시크릿 키를 이용하여 서명 생성. 체크섬 용도

### 위험요소

- 해커는 서버측의 시크릿키를 탈취하면 jwt 정보를 해킹할 수 있다
- 인증서의 만료 기한이 길면 해독의 확률이 높아진다
- 기한을 짧게 구성하면 사용자는 빈번하게 로그인 해야하고(불편함), 서버 측은 오버헤드가 발생한다

위의 이유로 만료시간 연장 전략 혹은 리프레쉬 토큰을 서버 측에 저장해서 이를 기반으로 토큰 기간을 갱신하는 전략을 사용한다


## TODO 주석 활용

- `TODO: 내용`
    - 해야할 작업
- `FIXME: 내용`
    - 오작동, 버그가 발생되는 코드
- `HACK: 내용`
    - 해결은 했으나, 우아하지 않다, 깔끔하지는 않다
- `XXX: 내용`
    - 이 부분은 큰 문제점, 오류를 가지고 있다

## 데이터베이스 

pool(풀링 기법)

- 백엔드 서버가 가동하면, 백엔드와 데이터베이스 간 일정량의 커넥션을 미리 맺음
- 큐(Queue: 선입선출) 구조에 담아서 관리
- 접속과 해제의 반복적인 작업에 따른 응답 시간 지연 원인을 제거, 일정량의 동접이 발생했을 때 안정적인 처리속도를 제공
- sqlalchemy

orm 방식

- 객체 지향 박식으로 코드에서 데이터베이스 연동, 데이터 처리 등을 관리
- 원칙적으로는 SQL을 몰라도 처리 가능
    - 데이터베이스 밴더가 교체되더라도 동일하게 작동
- 쿼리가 최적화되었다고 볼 수 없다: 기계적인 생성
- sqlalchemy, flask-migrate

- 코드

```python
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)
```

- 환경변수

```python
DB_PROTOCAL = "mysql+pymysql"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_DATABASE = "my_db"

SQLALCHEMY_DATABASE_URL = f"{DB_PROTOCAL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

- 데이터베이스 생성, 초기화(최초 1회)
    - sqlite: 소형 데이터베이스, 스마트폰에 사용하는 DB. 이 경우에는 데이터베이스 생성을 자동으로 해줌ㅡㅛㄴ비

```
flask --app service db init
```
migrations 폴더가 생긴다.(내부는 자동으로 만들어지는 구조이므로, 관여하지 않는다) 단, versions 밑으로 수정할 때마다 새로운 버전의 DB가 생성된다


- 모델(테이블) 생성, 변경

model > models.py에 테이블 내용 작성
```
flask --app service db migrate
```

- 모델(테이블) 생성, 변경 후 데이터베이스에 적용
```
flask --app service db upgrade
```

컨테이너 이미지 생성 시 위의 명령어 3개를 차례대로 수행해서 데이터베이스 초기화, 생성 과정을 수행

## 필요한 기능 시뮬레이션

- DBA는 sql문을 작성해서 쿼리 구현 
- ORM에서는 shell을 열어서 파이썬 코드로 구현
- flask --app service shell
