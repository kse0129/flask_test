from service import db

# 테이블 별로 클래스 설계
# 클래스 1개는 테이르 1개
# 클래스는 멤버 -> 테이블의 컬럼
# 클래스 객체 1개는 테이블의 row 데이터 1개

# 아래 테이블은 작성자 정보가 없는 익명 질문과 답변 게시판(과도기적 게시판)

# 질문 테이블
# String: 제한된 텍스트(varchar), Text: 제한없는 텍스트(text)
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)

# 답변 테이블
# question_id: 답변과 질문을 연결하기 위해 추가된 속성
# 어떤 질문에 대한 답변인지를 찾기 위해서 id 속성 추가(primary_key)
# 2개의 테이블을 연결하기 위해서 참조기 ForeignKey(외부키) 지정
# ondelete="CASCADE": 삭제 연동 옵션
# relationship(): 답변에 연결된 질문에 접근해서 정보 추출이 용이(answer.question.title)
# backref: 역참조. (answer.answer_set)
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE"))
    question = db.relationship("Question", backref=db.backref("answer_set"))
    content = db.Column(db.Text(), nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)