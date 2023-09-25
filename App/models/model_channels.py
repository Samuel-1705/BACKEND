from ..connection import DatabaseConnection

class Channel:
    _keys = ('channel_id', 'name', 'server_id', 'description')

    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.name = kwargs.get('name')
        self.server_id = kwargs.get('server_id')
        self.description = kwargs.get('description')

    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, channel):
        query = """INSERT INTO channels (name, server_id, description) VALUES (%(name)s, %(server_id)s, %(description)s)"""
        params = channel.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, channel):
        query = "DELETE FROM channels WHERE channel_id = %s"
        params = (channel.channel_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, channel = None):
        if channel and channel.channel_id:
            query = "SELECT channel_id, name, server_id, description FROM channels WHERE channel_id = %s"
            params = (channel.channel_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        elif channel and channel.server_id:
            query = "SELECT channel_id, name, server_id, description FROM channels WHERE server_id = %s"
            params = (channel.server_id,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        else:
            query = "SELECT channel_id, name, server_id, description FROM channels"
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]

    @classmethod
    def update(cls, channel):
        allowed_columns = {'name', 'description'}
        query_parts = []
        params = []
        for key, value in channel.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        
        # Add the task_item ID to be updated to the params list
        params.append(channel.channel_id)

        query = "UPDATE channels SET " + ", ".join(query_parts) + " WHERE channel_id = %s"

        DatabaseConnection.execute_query(query, tuple(params))