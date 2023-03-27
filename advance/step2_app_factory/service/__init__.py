# 사용자가 정의한 엔트리포인트
from flask import Flask

"""
    create_app은 플라스크 내부에서 정의된 함수명(수정X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할수 있다(모듈가져오기)
"""


def create_app():
    app = Flask(__name__)
    # 환경변수 초기화
    init_environment(app)
    # blueprint 초기화
    init_blueprint(app)

    return app


def init_environment(app):
    # 특정파일(cfg, ...)등을 읽어서 처리 가능
    app.config.from_pyfile('resource/config.cfg', silent=True)
    # py를 모듈 가져오기해서 객체를 세팅하여 처리
    import service.config as config
    app.config.from_object(config)

    print('\n' + '-'*20)

    # 환경변수(os, flask, 사용자 정의 레벨) 모두 출력
    # for k, v in app.config.items():
    #     print(k, v)

    # 개별 환경변수 추출
    # print(app.config['SECRET_KEY'], app.config.get('SECRET_KEY'))

    print('-'*20 + '\n')


def init_blueprint(app):
    # app에 blueprint 객체를 등록

    # blueprint로 정의된 개별 페이지 내용 로드
    from .controllers import main_controller

    # from service.controllers import main_bp
    # service 생략 가능
    from .controllers import main_bp

    # 플라스크 객체에 blueprint 등록
    app.register_blueprint(main_bp)

    from .controllers import auth_controller
    from .controllers import auth_bp
    app.register_blueprint(auth_bp)
