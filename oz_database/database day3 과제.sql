CREATE TABLE employees(
    id INT AUTO_INCRUMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);

SELECT name, salary FROM employees 





-- LAST_INSERT_ID() : 마지막으로 입력한 아이디 값 넣기


-- 생성 초급
-- (1) customers 테이블 고객 추가
INSERT INTO customers (name, age, address) VALUES ('Eric green', '24', 'Cheongju');

-- (2) products 테이블에 새 제품 추가
INSERT INTO  products (productId, name, price) VALUES (1, 'soju', '1600');

-- (3) employees 테이블에 새 직원 추가
INSERT INTO employees (name, age, job, employeeId) VALUES ('JaeHoon Park', 25, 'designer', 1);

-- (4) offices 테이블에 새 사무실 추가
INSERT INTO offices (name, city) VALUES ('Eric ma', 'Cheong ju');

-- (5) orders 테이블에 새 주문 추가
INSERT INTO orders (customerId, orderDate, hair) VALUES ('1', '24.04.11','cut');

-- (6) orderdetails 테이블에 주문 상세 정보 추가
INSERT INTO orderdetails(orderId,gender, date) VALUES (1, 'male cut', '24.04.17');

-- (7) payments 테이블에 지불 정보 추가
INSERT INTO  payments(payId, date, pay_by) VALUES (1, '24.04.17', 'card');

-- (8) productlines 테이블에 제품 라인 추가
INSERT INTO productlines (productline, help) VALUES ('hair cut', 'two block');

-- (9) customers 테이블 다른 지역 고객 추가
INSERT INTO customers (name, age, address)VALUES ('green kim', 23, 'Daejeon');

-- (10) products 테이블에 다른 카테고리의 제품 추가
INSERT INTO  products (productId, name, price) VALUES (2, 'beer', 2300);

-- 생성 중급
--(1) costomers 테이블 여러 고객 한번에 추가하기
INSERT INTO customers (name, age, address) VALUES ('Eric green', '24', 'Cheongju'), ('SeongRak', '2'5, 'Daejeon');

--(2) products 테이블에 여러 제품을 한번에 추가하세요
INSERT INTO  products (productId, name, price) VALUES (1, 'soju', '1600'), 





-- 읽기 초급
-- (1) customers 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;

-- (2) products 테이블에서 모든 제품 목록을 조회하세요.
SELECT * FROM products;

-- (3) employees 테이블에서 모든 직원의 이름과 나이을 조회하세요.
SELECT name, age FROM employees;

-- (4) offices 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT city FROM offices;

-- (5) orders 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

-- (6) orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE orderID = 1;

-- (7) payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customerId = 1;

-- (8) productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productline, help FROM productlines; 

-- (9) customers 테이블에서 특정 지역의 고객을 조회하세요.
SELECT * FROM customers WHERE city = 'cheong ju';

-- (10) products 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE Price BETWEEN 1000 AND 2000;

-- 읽기 중급
-- (1) order 테이블 특정고객 주문 조회
SELECT * FROM orders WHERE customerID = 1;

-- (2) orderdetails 테이블에서 특정 제품에 대한 모든 주문 상세정보를 조회하세요
SELECT * FROM orderdetails WHERE productID = 2;
-- 갱신 초급
-- (1) customer 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET city = 'Seoul' WHERE customerId = 1;
-- (2) products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET price = 1500 WHERE  productId = 1;
-- (3) employees 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees SET job = 'intern' WHERE employeeId = 1;
-- (4) offices 테이블에서 특정 사무실의 이름을 갱신하세요.
UPDATE offices SET name = 'juno hair' WHERE officeId = 1;
-- (5) orders 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET status = 'Delivery completed' WHERE orderId = 1;
-- (6) orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetailes SET OrderQuantity = 2 WHERE orderId = 1;
-- (7) payments 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET price = 3000 WHERE payId = 1;
-- (8) productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET help = 'one block' WHERE productline = 'hair cut' ;
-- (9) customers 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET email = 'asd@gma.com' WHERE customerId = 1;
-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET price = 3000;

-- 삭제 초급
-- (1) customers 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers WHERE customerId = 1;
-- (2) products 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE productId = 1;
-- (3) employees 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE employeesId = 1;
-- (4) offices 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE name = 'juno hair';
-- (5) orders 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE orderId = 1;
-- (6) orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderId= 1;
-- (7) payments 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE pay_by = 'card'; 
-- (8) productlines 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productline = 'hair cut' ;
-- (9) customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE city = 'cheongju' ;
-- (10) products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE category = 'shoes'; 
 
