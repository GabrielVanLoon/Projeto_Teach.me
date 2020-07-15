class Subject:
    def __init__(self, name=None, parent_subject=None):
        self.name = name
        self.parent_subject = parent_subject

    def __iter__(self):
        yield 'name',           name
        yield 'parent_subject', parent_subject
