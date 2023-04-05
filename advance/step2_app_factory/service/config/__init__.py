SECRET_KEY='8758e0d3ee6b14e48ed9733a5e2f6afe' # 서비스시 추론이 불가한 해시값

# ORM 처리를 위한 환경변수 설정(임의 설정)
DB_PROTOCAL = "mysql+pymysql"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_DATABASE = "my_db" # 이 서비스에서 사용할 데이터베이스명

# 이 환경변수는 migrate가 필수로 요구하는 환경변수
SQLALCHEMY_DATABASE_URI = f"{DB_PROTOCAL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# sqlalchemy 추가 설정
SQLALCHEMY_TRACK_MODIFICATIONS = False