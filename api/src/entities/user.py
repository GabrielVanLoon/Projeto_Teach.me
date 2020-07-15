class User:
    def __init__(self, username=None, email=None, password=None, name=None, last_name=None, picture=None, is_instructor=None):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
        self.picture = picture
        self.is_instructor = is_instructor

    def __iter__(self):
        yield 'username',   self.username
        yield 'email',      self.email
        yield 'password',   self.password
        yield 'name',       self.name
        yield 'last_name',  self.last_name
        yield 'picture',    self.picture
        yield 'is_instructor', self.is_instructor
