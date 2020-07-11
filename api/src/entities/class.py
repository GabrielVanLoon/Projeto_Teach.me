#Class eh nome reservado em python, entao decidimos trocar por StudyClass
class Class:
    def __init__(self, classname=None, title=None, description=None, image=None, members_qtt=None, max_members=None, situation=None):
        self.classname = classname
        self.title = title
        self.description = description
        self.image = image
        self.members_qtt = members_qtt
        self.max_members = max_members
        self.situation = situation
