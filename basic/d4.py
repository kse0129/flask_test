'''
데이터 베이스 접속 후 쿼리 수행 + 파라미터 전달
'''
import pymysql

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
        cursor.execute(sql, ('guest', '1234'))
        row = cursor.fetchone()
        print('사용자 이름:', row['name'])

except Exception as e:
    print('접속 오류', e)
else:
    print('접속 성공')
finally:
    if connection:
        connection.close()
        print('접속 종료 성공')