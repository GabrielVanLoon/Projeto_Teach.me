class Offer:
    def __init__(self, instructor=None, subject=None, base_price=None, methodology=None):
        self.instructor = instructor
        self.subject = subject
        self.base_price = base_price
        self.methodology = methodology

    def __iter__(self):
        yield 'instructor',   self.instructor
        yield 'subject',      self.subject
        yield 'base_price',   self.base_price
        yield 'methodology',  self.methodology