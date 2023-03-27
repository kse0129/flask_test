# 애플리케이션 구동
- flask 명령상 기본으로 찾는 파일, 여러개가 존재할 시 우선순위
    - wsgi.py
    - app.py
    - 환경변수에 지정된 파일(FLASK_APP=xxx)을 찾는다


- 커스텀 설정
    1. 환경변수를 지정 후 실행: OS를 설정하거나 shell or cmd를 작성해서 구동
        ```
        set FLASK_APP=start_app
        flask run
        ```

    2. 환경변수 파일을 읽어서 처리
        - 설치
        ```
        conda install python-dotenv -y
        ```
        - 파일 생성
            - env.config
            - start_app.py

    3. 명령 수행시 옵션 제공
        ```
        flask --app start_app run
        flask --app start_app --debug run
        ```


# 실습
1. wsgi.py 파일 생성
2. flask run
```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```