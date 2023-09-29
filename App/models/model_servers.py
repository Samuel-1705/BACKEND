from ..connection import DatabaseConnection

class Server:
    _keys = ['server_id', 'name', 'description','icon']
    
    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.icon = kwargs.get('icon')
        
    
    def serialize(self):
        return {
            'server_id':self.server_id,
            'name' : self.name,
            'description' : self.description,
            'icon' : self.icon
        }
        
    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, server):
        query ="""INSERT INTO servers(name,description,icon) VALUES (%(name)s, %(description)s, %(icon)s)"""
        params = server.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, server):
        query = "DELETE FROM servers WHERE server_id = %s"
        params = (server.server_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, server = None):
        if server and server.server_id:
            query = "SELECT server_id, name, description, icon FROM team.servers WHERE server_id = %s"
            params = (server.server_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        else:
            query = """SELECT server_id, name, description, icon FROM servers"""
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        
    @classmethod
    def update(cls, server):
        allowed_columns = {'name', 'description', 'icon'}
        query_parts = []
        params = []
        for key, value in server.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        
        params.append(server.server_id)
        query = "UPDATE servers SET " + ", ".join(query_parts) + " WHERE server_id = %s"
        DatabaseConnection.execute_query(query, params)
        
    classmethod
    def get_users(server):
        query = """SELECT u.user_id, u.username, u.password, u.email, u.profile_image
                FROM team.users u 
                INNER JOIN team.server_onboarding so ON u.user_id = so.user_id 
                WHERE so.server_id = %(server_id)s"""
        params = server.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        users=[]
        from .model_users import User
        for row in results:
            users.append(User(**dict(zip(User._keys, row))))
        return users