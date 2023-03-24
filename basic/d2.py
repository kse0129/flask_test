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
                                # cursorclass=pymysql.cursors.DictCursor 
                                # 조회 결과는 딕셔너리 리스트 형태, 생략할 시 튜플 리스트 형태
                                )
    # 쿼리 수행: pymysql은 커서를 획득해서 쿼리를 수행
    # 1. 커서 획득
    # connection.cursor(pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        # 2. SQL문 준비
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
        # 3. SQL 쿼리 수행
        cursor.execute(sql)
        # 4. 결과 획득
        row = cursor.fetchone()
        # 5. 결과 확인
        # 튜플로 결과를 받으면 순서에 의해 인덱싱하므로 리스크가 있음
        print('사용자 이름:', row[1])

except Exception as e:
    print('접속 오류', e)
else:
    print('접속 성공')
finally:
    if connection:
        connection.close()
        print('접속 종료 성공')