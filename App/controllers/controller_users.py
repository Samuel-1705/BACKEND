from ..models.model_users import User

from flask import request, session,jsonify

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
    
    @classmethod
    def login(cls):
        data = request.json
        user = User(
            username = data.get('username'),
            email = data.get('email'),
            password = data.get('password')
        )
        if User.is_registered(user):
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario, contraseña o Email incorrectos"}, 401
        
    @classmethod
    def get_servers(cls, user_id):
        user = User(user_id=user_id) 
        servers=[]   
        for server in User.get_servers(user):
            servers.append(server.serialize())
        return servers, 200
    
