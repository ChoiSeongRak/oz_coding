-- (1) 테이블 생성
CREATE TABLE employees(
    id INT AUTO_INCRUMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);
-- (2) 직원 데이터 추가
INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontend', 80000);
INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

-- (3) 모든 직원의 이름과 연봉 조회
SELECT name, salary FROM employees 

-- (4) 프론트 엔드 직책을 가진 직원 중 연봉이 90000 이하인 직원의 이름과 연봉 조회
SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

--(5) PM 직책을 가진 직원들 연봉 10% 인상 후 조회
UPDATE employees SET salary = salary * 1.1 WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM'

--(6) 백엔드 직책을 가진 직원들 연봉 5% 인상 
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

--(7) 민혁 사원 데이터 삭제
DELETE FROM employees WHERE name = '민혁';

-- (8) 모든 직원을 직책별로 그룹화하여 각 직책의 평균 연봉 계산
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

-- (9) 테이블 삭제
DELETE TABLE employees;
