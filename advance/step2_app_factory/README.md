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