from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint("Users", "users", description = "Operations on users", url_prefix='/user')

# API LIST :
# (1) 전체 유저 데이터 조회 (GET)
# (2) 유저 생성 (POST)
@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        
        # for user in users:
        #     print(user.id)
        #     print(user.name)
        #     print(user.email)
        
        user_data = [
            {'id':user.id, 'name':user.name, 'email':user.email} for user in users
        ]
        return jsonify(user_data)
    
    def post(self):
        data = request.json # 유저가 보낸 데이터
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"msg":"Successfully created new user"}), 201
    
@user_blp.route("/<int:user_id>")
class UserResource(MethodView):
    
# (1) 특정 유저 데이터 조회(GET)
    def get(self,user_id):
        user = User.query.get_or_404(user_id)

        return jsonify({
            "name":user.name,
            "email":user.email
        })
        
    def put(self,user_id):
        user = User.query.get_or_404(user_id)
        data = request.json
        
        user.name = data['name']
        user.email = data['email']
        
        db.session.commit()
        
        return jsonify({'msg':'Successfully updated user data'}), 201
# (3) 특정 유저 삭제 (DELETE)
    def delete(self,user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({"msg":"Succeessfully deleted user data"}), 201