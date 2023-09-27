from ..connection import DatabaseConnection

class User:
    _keys = ['user_id', 'username', 'password','email','profile_image']
    
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.profile_image = kwargs.get('profile_image')
    
    def serialize(self):
        return {
            'user_id':self.user_id,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'profile_image': self.profile_image
        }
        
    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, user):
        query ="""INSERT INTO team.users(username,password,email,profile_image) VALUES (%(username)s, %(password)s, %(email)s,%(profile_image)s)"""
        params = user.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, user):
        query = "DELETE FROM users WHERE user_id = %s"
        params = (user.user_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, user = None):
        if user and user.user_id:
            query = "SELECT user_id, username, password, email,profile_image FROM team.users WHERE user_id = %s"
            params = (user.user_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        else:
            query = """SELECT user_id, username, password, email,profile_image FROM users"""
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        
    @classmethod
    def update(cls, user):
        allowed_columns = {'username', 'password', 'email', 'profile_image'}
        query_parts = []
        params = []
        for key, value in user.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        
        params.append(user.user_id)
        query = "UPDATE users SET " + ", ".join(query_parts) + " WHERE user_id = %s"
        DatabaseConnection.execute_query(query, params)
        
        
        
    @classmethod    
    def is_registered(cls, user):
        query = """SELECT user_id FROM Team.users 
        WHERE username = %(username)s and email= %(email)s and password = %(password)s """
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
""" @classmethod
def get_servers(cls, user):
    
        """