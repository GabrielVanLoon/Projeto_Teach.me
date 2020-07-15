class Place:
    def __init__(self, instructor=None, placename=None, capacity=None, street=None, number=None, neighborhood=None, complement=None, city=None, federal_state=None):
        self.instructor = instructor
        self.placename = placename
        self.capacity = capacity
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.complement = complement
        self.city = city
        self.federal_state = federal_state

    def __iter__(self):
        yield instructor,   instructor
        yield placename,    placename
        yield capacity,     capacity
        yield street,       street
        yield number,       number
        yield neighborhood, neighborhood
        yield complement,   complement
        yield city,         city
        yield federal_state, federal_state