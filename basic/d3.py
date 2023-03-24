'''
데이터 베이스 접속 후 쿼리 수행
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
        sql = """
            SELECT
                uid, `name`, regdate
            FROM
                users
            WHERE
                uid='guest'
            AND
                upw='1234';
        """
        cursor.execute(sql)
        row = cursor.fetchone()
        # 딕셔너리 결과값 -> key로 value반환
        print('사용자 이름:', row['name'])

except Exception as e:
    print('접속 오류', e)
else:
    print('접속 성공')
finally:
    if connection:
        connection.close()
        print('접속 종료 성공')