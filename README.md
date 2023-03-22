# 파이썬 기반 웹 프로그래밍

# 목표
    - 웹 환경 이해 및 웹 프로그램 구성
    - Flask 웹 기반 백엔드(서버) 프로그래밍
    - blueprint를 이용한 기능별 분할 구성
    - 데이터베이스 연동(SQL, ORM)
    - 배포 및 운영

# 발전적 목표
    - 머신러닝(딥러닝 포함) 모델 서빙 및 서비스를 구현
    - 구축된 서비스를 도커 및 쿠버네티스 기반에서 운영
    - MLOps에 연동 사용

# 가상환경 구축
    - 순수 파이썬
        1. 가상환경을 모아두는 폴더 생성
            - mkdir venvs
        2. 해당 폴더로 이동
            - cd venvs
        3. 가상환경 생성
            - python -m venv venv_name
    - 아나콘다(미니콘다, ...)

# 필요한 패키지 설치
    - requirements.txt 생성
    - 작성
        - 수동 : 패키지(==version) 직접 기입
        - 자동 : pip freeze > requirements.txt
    - 설치
        - pip install -r requirements.txt