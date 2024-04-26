from pymongo import MongoClient
from datetime import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client.local


# 특정 장르의 책 찾기
def find_books_by_genre(db, genre):
    books_ = db.books.find({"genre": genre}, {"title": 1, "author": 1})
    for book in books_:
        print(book)
find_books_by_genre(db,"fantasy")

# 감독별 평균 영화 평점 계산
def calc_dir_rating_avg(db):
    movie_collection = db.movies
    total = [
        {"$group": {"_id" : "$director", "avg_rating": {"$avg":"$rating"}}},
        {"$sort": {"avg_rating": -1}}    
            ]
    results = movie_collection.aggregate(total)
    for result in results:
        print(result)
calc_dir_rating_avg(db)

# 특정 사용자의 최근 행동 조회
def find_user_recent_actions(db, user_id):
    user_actions_collection = db.user_actions
    cond =[{"$match": {"user_id":user_id}},
           {"$sort": {"timestamp":-1}},
           {"$limit":5}
    ]
    results = user_actions_collection.aggregate(cond)
    for result in results:
        print(result)
find_user_recent_actions(db,1)

# 출판 연도별 책의 수 계산
def calc_books_pub_year(db):
    books_collection = db.books
    cond = [
        {"$group":{"_id": "$year","count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    results = books_collection.aggregate(cond)
    for result in results:
        print(result)
calc_books_pub_year(db)

# 특정 사용자의 행동 유형 업데이트
def update_user_actions(db,user_id,date,old_action,new_action):
    user_actions_collection = db.user_actions
    cond = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
    update = {"$set": {"action": new_action}}
    
    results = user_actions_collection.update_many(cond, update)
    print(results.modified_count)
    
update_user_actions(db,1,datetime(2023,4,10), "view", "seen")



    
    
    
    
    



    
    


# def insert_data():
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client.local  # 'local' 데이터베이스 사용

#     # 책 데이터 삽입
#     books = [
#         {
#             "title": "Kafka on the Shore",
#             "author": "Haruki Murakami",
#             "year": 2002,
#             "genre": "fantasy",
#         },
#         {
#             "title": "Norwegian Wood",
#             "author": "Haruki Murakami",
#             "year": 1987,
#             "genre": "thriller",
#         },
#         {
#             "title": "1Q84",
#             "author": "Haruki Murakami",
#             "year": 2009,
#             "genre": "fantasy",
#         }
#     ]
#     db.books.insert_many(books)

#     # 영화 데이터 삽입
#     movies = [
#         {
#             "title": "Inception",
#             "director": "Christopher Nolan",
#             "year": 2010,
#             "rating": 8.8,
#             "genre": "fantasy",
#         },
#         {
#             "title": "Interstellar",
#             "director": "Christopher Nolan",
#             "year": 2014,
#             "rating": 8.6,
#             "genre": "fantasy",
#         },
#         {
#             "title": "The Dark Knight",
#             "director": "Christopher Nolan",
#             "year": 2008,
#             "rating": 9.0,
#             "genre": "fantasy",
#         },
#     ]
#     db.movies.insert_many(movies)

#     # 사용자 행동 데이터 삽입
#     user_actions = [
#         {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
#         {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
#         {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"}
#     ]
#     db.user_actions.insert_many(user_actions)

#     print("Data inserted successfully")
#     client.close()

# if __name__ == "__main__":
#     insert_data()