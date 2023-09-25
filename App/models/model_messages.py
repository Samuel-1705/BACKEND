from ..connection import DatabaseConnection

class Message:
    _keys = ('message_id', 'user_id', 'channel_id', 'content','creation_date')

    def __init__(self, **kwargs):
        self.message_id = kwargs.get('message_id')
        self.user_id = kwargs.get('user_id')
        self.channel_id = kwargs.get('channel_id')
        self.content = kwargs.get('content')
        self.creation_date = kwargs.get('creation_date')

    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, message):
        query = """INSERT INTO messages (user_id, channel_id, content,creation_date) VALUES (%(user_id)s, %(channel_id)s, %(content)s,%(creation_date)s)"""
        params = message.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, message):
        query = "DELETE FROM messages WHERE message_id = %s"
        params = (message.message_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, message = None):
        if message and message.message_id:
            query = "SELECT message_id, user_id, channel_id, content,creation_date  FROM messages WHERE message_id = %s"
            params = (message.message_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        elif message and message.user_id:
            query = "SELECT message_id, user_id, channel_id, content,creation_date FROM messages WHERE user_id = %s"
            params = (message.user_id,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        elif message and message.channel_id:
            query = "SELECT message_id, user_id, channel_id, content,creation_date FROM messages WHERE channel_id = %s"
            params = (message.channel_id,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        else:
            query = "SELECT message_id, user_id, channel_id, content,creation_date FROM messages"
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]

    