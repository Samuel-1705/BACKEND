from ..models.model_messages import Message
import datetime
from flask import request, session,jsonify

class MessageController:
    @classmethod
    def get(cls):
        Messages = []
        if request.args.get('message_id'):
            Message_obj = Message(message_id=request.args.get('message_id'))
            Messages = Message.get(Message_obj)
        else:
            Messages = Message.get()
        return [Message.to_dict() for Message in Messages], 200

    @classmethod
    def get_id(cls, message_id):
        Message_obj = Message(message_id=message_id)
        message = Message.get(Message_obj)
        if message:
            return jsonify(message.to_dict()), 200

    @classmethod
    def create(cls):
        data = request.json
        creation_dates=datetime.date.today()
        Message_obj = Message(user_id=data['user_id'], channel_id=data['channel_id'],content=data.get('content'),creation_date=creation_dates )
        Message.create(Message_obj)
        return {'message': 'Message item created successfully'}, 201
    
    @classmethod
    def delete(cls, message_id):
        Message_obj = Message(message_id=message_id)
        Message.delete(Message_obj)
        return {'message': 'Message deleted successfully'}, 200
