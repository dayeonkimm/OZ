use testdatabase;

# 1. employee 테이블 생성
-- CREATE TABLE employees(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10,2)
-- );

# 2. 직원 데이터 추가
-- INSERT INTO employees (name, position, salary) 
-- VALUES ('혜린','PM',90000), 
-- ('은우', 'Frontend', 80000),
-- ('가을', 'Backend', 92000),
-- ('지수', 'Frontend', 78000),
-- ('민혁', 'Frontend', 96000),
-- ('하온', 'Backend', 130000);

# 3. 모든 직원의 이름과 연봉 정보 조회
-- SELECT name, salary FROM employees;

# 4. Frontend 중 연봉 90000 이하 직원 이름, 연봉 조회
-- SELECT name, salary FROM employees WHERE position = 'Frontend' and salary <= 90000;

# 5. PM 직원 연봉 10% 인상 후 결과 조회
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE position = 'PM';

-- SELECT * FROM employees WHERE position = 'PM';

# 5. Backend 연봉 5% 인상
-- UPDATE employees
-- SET salary = salary * 1.05
-- WHERE position = 'Backend';

# 7. 민혁 사원 데이터 삭제
-- DELETE FROM employees WHERE name = '민혁';

# 8. 모든 직원 position 별로 그룹화 후 직책 평균 연봉 계산
-- SELECT position, AVG(salary) AS avgSalary FROM employees
-- GROUP BY position;

# 9. employees 테이블 삭제
-- DROP TABLE employees;
