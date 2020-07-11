class User:
    def __init__(self, username=None, email=None, password=None, name=None, last_name=None, picture=None, is_instructor=None):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
        self.picture = picture
        self.is_instructor = is_instructor
