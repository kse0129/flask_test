'''
파이썬 <-> 데이터베이스
파이썬으로 데이터베이스를 엑세스하여 쿼리를 전송, 수행결과를 받아오는 방식
    - SQL 수행
        - basic에서 수행
        - pymysql 패키지 사용
            - https://github.com/PyMySQL/PyMySQL
    - ORM 수행
        - advance에서 수행

업무 포지션은 지원팀, 공용 API를 만드는 파트 -> 함수, 클래스 형태로 라이브러리 제공
사용방법에 대한 예제까지 제공

데이터베이스를 터미널을 통해서 접속
1. root 권한으로 mysql 접속
    $ mysql -u root -p
    Enter Password: ****
    MariaDB [(none)]>
2. 데이터베이스 생성
    CREATE DATABASE ml_db;
3. 데이터베이스 목록 출력
    SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | ml_db              |
    | mysql              |
    | new_data_db        |
    | performance_schema |
    | sys                |
    +--------------------+
4. 현재 작업(사용)할 데이터베이스 지정
    MariaDB [(none)]> USE ml_db;
    Database changed
    MariaDB [ml_db]> SHOW TABLES;

5. 고객 테이블 생성
    CREATE TABLE `users` (
        `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 관리번호',
        `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 아이디' COLLATE 'utf8mb4_general_ci',
        `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비밀번호' COLLATE 'utf8mb4_general_ci',
        `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci',
        `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일',
        PRIMARY KEY (`id`) USING BTREE,
        UNIQUE INDEX `uid` (`uid`) USING BTREE
    )
    COMMENT='고객 테이블'
    COLLATE='utf8mb4_general_ci'
    ENGINE=InnoDB
    ;

    ALTER TABLE `users`
	CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 관리번호' FIRST,
	CHANGE COLUMN `uid` `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 아이디' COLLATE 'utf8mb4_general_ci' AFTER `id`,
	CHANGE COLUMN `upw` `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비밀번호' COLLATE 'utf8mb4_general_ci' AFTER `uid`,
	CHANGE COLUMN `name` `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
	CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일' AFTER `name`;


'''
import pymysql