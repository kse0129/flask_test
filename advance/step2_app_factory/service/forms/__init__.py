"""
    wtf를 활용하여 Form을 디자인(FlaskForm을 상속받아서 재정의)
"""
from flask_wtf import FlaskForm
# 데이터베이스상 테이블의 컬럼 타입과 연관을 맺는다
# StringField: varchar(32) -> 글자수 제한이 있는 데이터를 받을 때 지정
# TextAreaField: text -> 글자수 제한이 없는 경우. ex) 65535개 글자 수 등의 제한이 있긴함
from wtforms import StringField, TextAreaField
# 유효성 검사용 옵션 가져오기
from wtforms.validators import DataRequired, Length, Email

class FormQuestion(FlaskForm):
    # 클래스 변수만 지정
    # 변수명 -> html태그의 id, name값
    # 첫번째 인자 -> label값 
    title = StringField('제목', validators=[DataRequired('필수 입력란입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('')])