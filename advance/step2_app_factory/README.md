# 애플리케이션 팩토리
엔트리 위치 조정, 코드 조정
```python
app = Flask(__name__)
```
- 현재 위의 코드는 전역변수로 존재
- 프로젝트 규모가 커지면, 순환 참조를 할 확률이 큼
- Flask 객체는 애플리케이션 팩토리라는 형태로 사용 권장

# 방법
플라스크 객체를 생성하는 코드를 특정 패키지 밑에 위치 후 `__init__.py`로 파일 이름 변경
```
service
L __init__.py
```
최종 실행 명령
```
flask --app service --debug run
```

# 블루프린트
url과 함수의 매핑(라우트)을 관리하는 도구

# 부트스트랩
부트스트랩을 적용하여 페이지를 구성한다. flask-bootstrap은 2017년 이후로 업데이트되고 있지 않다.

1. 부트스트랩 [다운로드](https://getbootstrap.kr/docs/5.2/getting-started/download/)

2. 압축 해제 후 static 폴더에 bootstrap.min.css, bootstrap.min.js 이동

다양한 UI 형태를 [예시](https://getbootstrap.kr/docs/5.2/examples/)로 제공하고 있다.