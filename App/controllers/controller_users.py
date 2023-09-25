from ..models.model_users import User

from flask import request, session,jsonify,json

class UserController:

    @classmethod
    def get(cls):
        users = User.get()
        return [user.to_dict() for user in users], 200

    @classmethod
    def get_id(cls, user_id):
        user_obj = User(user_id = user_id)
        user = User.get(user_obj)
        if user:
            return jsonify(user.to_dict()), 200

    @classmethod
    def create(cls):
        data = request.json
        user_obj = User(username=data['username'], password=data['password'], email=data['email'], profile_image=data['profile_image'])
        User.create(user_obj)

        return {'message': 'User created successfully'}, 201


    @classmethod
    def update(cls, user_id):
        data = request.json
        user_obj = User(
            user_id=user_id,
            email=data.get('email'),
            password=data.get('password'),
            profile_image=data.get('profile_image'),
            username=data.get('username')
            )
        User.update(user_obj)
        return {'message': 'User updated successfully'}, 200

    @classmethod
    def delete(cls, user_id):
        user_obj = User(user_id=user_id)
        User.delete(user_obj)
        return {'message': 'User deleted successfully'}, 200