from flask import Blueprint

# 메인 서비스 페이지: A개발자 담당 -> ~/main/~
main_bp = Blueprint('main_bp',      # 별칭, 해당 블루프린트 밑에서 정의된 라우트 및 함수를 url_for()로 지칭할 때 사용. url_for('main_bp.home')
                    __name__,                       # 고정
                    url_prefix='/main',             # 모든 url 앞에 /main이 추가된다
                    template_folder='../templates', # html이 위치하는 폴더 지정
                    static_folder='../static'       # 정적데이터가 위치하는 폴더 지정
                    )

# 메인 서비스 페이지: A개발자 담당 -> ~/auth/~
auth_bp = Blueprint('auth_bp',      # 별칭, 해당 블루프린트 밑에서 정의된 라우트 및 함수를 url_for()로 지칭할 때 사용. url_for('main_bp.home')
                    __name__,                       # 고정
                    url_prefix='/auth',             # 모든 url 앞에 /main이 추가된다
                    )