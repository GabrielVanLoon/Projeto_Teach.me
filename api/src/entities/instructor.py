class Instructor:
    def __init__(self, username=None, abstract=None, about_me=None, degree=None):
        self.username = username
        self.abstract = abstract
        self.about_me = about_me
        self.degree = degree

    def __iter__(self):
        yield 'username', self.username
        yield 'abstract', self.abstract
        yield 'about_me', self.about_me
        yield 'degree',   self.degree