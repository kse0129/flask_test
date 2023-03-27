# 파이썬 기반 웹 프로그래밍

## 목표
- 웹 환경 이해 및 웹 프로그램 구성
- Flask 웹 기반 백엔드(서버) 프로그래밍
- blueprint를 이용한 기능별 분할 구성
    - 회원 관련 업무(가입, 로그인, 로그아웃, 탈퇴, 세션관리, 쿠키, ...) : A 개발자가 담당
    - 모델 서빙 파트(데이터 전처리, 모델 예측 수행, 응답처리, ...) : B 개발자가 담당
    - 데이터베이스 관련 업무(SQL or ORM, API, DB 준비) : C 개발자가 담당
- 데이터베이스 연동(SQL, ORM)
- 배포 및 운영
    - 실제 회사라면 개발팀이 개발 완료시 운영팀에 전달 -> 운영팀이 세팅, 운영, 유지보수 진행

## 단계
1. 기획
2. 스토리보드
3. 디자인 시안, 데이터베이스 모델링, 프로토타입
4. 분야별
    - 프론트
        - 디자인 진행(페이지 단위 계산), html 코딩, 스크립트 처리
        - React, Vue, Angular : 전면 부분 구성
    - 백엔드
        - 기능별 구현
            - 페이지별 진행
            - 모델 서빙, 머신러닝 관련 서비스 기능 삽입
            - 데이터 분석, 시각화 : 파이썬 기반
        - 공통 기능 구현
        - 통신 프로토콜 구현
            - 요청과 응답 정리
    - 데이터 베이스
        - DB 설계
        - 테이블 구성
        - 쿼리 구성




## 발전적 목표
- 머신러닝(딥러닝 포함) 모델 서빙 및 서비스를 구현
- 구축된 서비스를 도커 및 쿠버네티스 기반에서 운영
- MLOps에 연동 사용

## 가상환경 구축
- 순수 파이썬
    1. 가상환경을 모아두는 폴더 생성
        - mkdir venvs
    2. 해당 폴더로 이동
        - cd venvs
    3. 가상환경 생성
        - python -m venv venv_name
- 아나콘다(미니콘다, ...)

## 필요한 패키지 설치
- `requirements.txt` 생성
- 작성
    - 수동: 패키지(==version) 직접 기입
    - 자동: `pip freeze > requirements.txt`
- 설치
    ```
    pip install -r requirements.txt
    ```

- pip
    - pip 입력시 command와 option에 대한 안내
    - ex) pip show pandas -> WARNING: Package(s) not found: pandas

## 데이터베이스 연동
- 1단계 코드 : 요청시 디비 접속, 쿼리 수행, 접속 해제 => 접속/해제 반복으로 인한 속도 저하문제 존재, 접속이 몰리면 서비스 지연 문제 발생, 다만 쉽게 구현 가능
- 2단계 코드 : 서버 가동시 sqlalchemy Pool을 이용하여 동접수를 계산하여 커넥션을 생성, 
                요청시 -> 풀에서 커넥션 획득(큐) -> 쿼리 수행 -> 커넥션 반납
                서버 종료시 Pool에 있는 모든 커넥션 해제(반납)
- 3단계 코드 : flask-migrate -> sqlalchemy -> ORM을 이용하여 객체지향적으로 쿼리 수행
                SQL 몰라도됨, 데이터베이스 제품이 변경되도 동일하게 작동,  SQL을 자동으로 생성해줌