from ..models.model_channels import Channel

from flask import request, session,jsonify

class ChannelController:
    @classmethod
    def get(cls):
        Channels = []
        if request.args.get('channel_id'):
            Channels_obj = Channel(channel_id=request.args.get('channel_id'))
            Channels = Channel.get(Channels_obj)
        else:
            Channels = Channel.get()
        return [Channel.to_dict() for Channel in Channels], 200

    @classmethod
    def get_id(cls, channel_id):
        channel_obj = Channel(channel_id=channel_id)
        channel = Channel.get(channel_obj)
        if channel:
            return jsonify(channel.to_dict()), 200

    @classmethod
    def create(cls):
        data = request.json
        channel_obj = Channel(name=data['name'], server_id=data['server_id'],description=data.get('description') )
        Channel.create(channel_obj)
        return {'message': 'Channel item created successfully'}, 201

    @classmethod
    def update(cls, channel_id):
        data = request.json
        channel_obj = Channel(
            channel_id=channel_id,
            name=data.get('name'),
            server_id=data.get('server_id'),
            description=data.get('description')
            )
        Channel.update(channel_obj)
        return {'message': 'Channel item updated successfully'}, 200

    @classmethod
    def delete(cls, channel_id):
        channel_obj = Channel(channel_id=channel_id)
        Channel.delete(channel_obj)
        return {'message': 'Task item deleted successfully'}, 200