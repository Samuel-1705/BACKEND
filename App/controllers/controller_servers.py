from ..models.model_servers import Server

from flask import request, session,jsonify

class ServerController:
    @classmethod
    def get(cls):
        servers = Server.get()
        return [server.to_dict() for server in servers], 200

    @classmethod
    def get_id(cls, server_id):
        server_obj = Server(server_id = server_id)
        server = Server.get(server_obj)
        if server:
            return jsonify(server.to_dict()), 200

    @classmethod
    def create(cls):
        data = request.json
        server_obj = Server(name=data['name'], description=data.get('description'), icon=data['icon'])
        Server.create(server_obj)

        return {'message': 'Server created successfully'}, 201


    @classmethod
    def update(cls, server_id):
        data = request.json
        server_obj = Server(
            server_id=server_id,
            name=data.get('name'),
            description=data.get('description'),
            icon=data.get('icon'),
            )
        Server.update(server_obj)
        return {'message': 'Server updated successfully'}, 200

    @classmethod
    def delete(cls, server_id):
        server_obj = Server(server_id=server_id)
        Server.delete(server_obj)
        return {'message': 'Server deleted successfully'}, 200