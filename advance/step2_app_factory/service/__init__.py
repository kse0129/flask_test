# 사용자가 정의한 엔트리포인트
from flask import Flask

'''
    create_app은 플라스크 내부에서 정의된 함수명(수정X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할수 있다(모듈가져오기)
'''

def create_app():
    app = Flask(__name__)

    init_blueprint(app)
    
    return app

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