import pymysql
from faker import Faker
import random

# Faker 객체 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='4682',  # 데이터베이스 비밀번호
    db='testdatabase',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


# # Products 테이블을 위한 더미 데이터 생성
# def generate_product_data(n):
#     for _ in range(n):
#         product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
#         price = round(random.uniform(10, 100), 2)
#         stock_quantity = random.randint(10, 100)
#         create_date = fake.date_time_this_year()
#         yield (product_name, price, stock_quantity, create_date)

# # Customers 테이블을 위한 더미 데이터 생성
# def generate_customer_data(n):
#     for _ in range(n):
#         customer_name = fake.name()
#         email = fake.email()
#         address = fake.address()
#         create_date = fake.date_time_this_year()
#         yield (customer_name, email, address, create_date)

# # Orders 테이블을 위한 더미 데이터 생성
# def generate_order_data(n, customer_ids):
#     for _ in range(n):
#         customer_id = random.choice(customer_ids)
#         order_date = fake.date_time_this_year()
#         total_amount = round(random.uniform(20, 500), 2)
#         yield (customer_id, order_date, total_amount)

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    # # 실전 연습문제
    # # (1) 세로운 재품 추가
    Book = 'Python Book'
    sql = f"INSERT INTO Products (productName, price, stockQuantity) VALUES ('{Book}', {29.99}, {30})"
    cursor.execute(sql)
    conn.commit()
    # (2) 고객 목록 조회
    sql = "SELECT * FROM Customers"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    # (3) 제품 재고 업데이트
    sql = "UPDATE Products SET stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql, quantity_order, product_id)
    conn.commit()
    
    # (4) 고객별 총 주문 금액 계산
    sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
    cursor.execute(sql)
    for row in cursor.fetchall(): 
						print(row)
 
    # (5)고객 이메일 업데이트
    sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    cursor.execute(sql, (new_email, customer_id))
    conn.commit()
    
    # (6) 주문 취소
    sql = "DELETE FROM Orders WHERE orderID = %s"
    cursor.exxcute(sql,(order_id,))
    conn.commit()
    
    # (7) 특정 제품 검색
    sql = "SELECT * FROM Products WHERE productName = %s"
    cursor.execute(sql, (product_name,))
    
    # (8) 특정 고객의 모든 주문 조ghl
    sql = "SELECT * FROM Orders WHERE customerID = %s"
    cursor.execute(sql, (customer_id,))
    for row in cursor.fetchall():
        print(row)
            
    # (9) 가장 많이 주문한 고객 찾기
    sql = "SELECT customerID, COUNT(*) as orderCount FROM Orders GROUP BY customerID ORDER BY oderCount DESC LIMIT 1"
    cursor.execute(sql)
    conn.commit()
    
    
    
    
    # # Products 데이터 삽입
    # products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    # for data in generate_product_data(10):
    #     cursor.execute(products_sql, data)
    # conn.commit()

    # # Customers 데이터 삽입
    # customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    # for data in generate_customer_data(5):
    #     cursor.execute(customers_sql, data)
    # conn.commit()

    # # Orders 데이터 삽입
    # # Customers 테이블에서 ID 목록을 얻어옵니다.
    # cursor.execute("SELECT customerID FROM Customers")
    # customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    # orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    # for data in generate_order_data(15, customer_ids):
    #     cursor.execute(orders_sql, data)
    # conn.commit()

# 데이터베이스 연결 종료
conn.close()