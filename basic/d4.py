'''
데이터 베이스 접속 후 쿼리 수행 + 파라미터 전달
'''
import pymysql

def login_db(user_id='', user_pw=''):
    connection = None
    try:
        connection = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='1234',
                                    database='ml_db',
                                    cursorclass=pymysql.cursors.DictCursor 
                                    )
        with connection.cursor() as cursor:
            # 파라미터는 %s 로 세팅 
            sql = """
                SELECT
                    uid, `name`, regdate
                FROM
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            """
            # execute() 함수의 2번 인자가 파라미터를 전달: 튜플의 형태
            cursor.execute(sql, (user_id, user_pw))
            row = cursor.fetchone()
            if row:
                print('회원입니다. 사용자 이름:', row['name'])
            else:
                print('회원이 아닙니다.')
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속 성공')
    finally:
        if connection:
            connection.close()
            print('접속 종료 성공')

if __name__ == "__main__":
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할 때는 작동하지 않음
    login_db()