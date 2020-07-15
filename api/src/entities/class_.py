class Class:
    def __init__(self, classname=None, title=None, description=None, image=None, members_qtt=None, max_members=None, situation=None):
        self.classname = classname
        self.title = title
        self.description = description
        self.image = image
        self.members_qtt = members_qtt
        self.max_members = max_members
        self.situation = situation

    def __iter__(self):
        yield 'classname',      classname
        yield 'title',          title
        yield 'description',    description
        yield 'image',          image
        yield 'members_qtt',    members_qtt
        yield 'max_members',    max_members
        yield 'situation',      situation