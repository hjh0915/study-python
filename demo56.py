class Airplane:
    """
    Information about a particular airplane including the model, the serial
    number, the number of seats, and the number of miles travelled.
    """

    def __init__(self, plane_model, serial_num, num_seats, miles_travelled):
        """ (Airplane, str, str, int, float)

        Record the airplane's model plane_model, serial number serial_num, the
        number of seats, and the distance travelled miles_travelled.

        >>> airplane = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> airplane.model
        'Boeing 747'
        >>> airplane.serial
        '19643'
        >>> airplane.seats
        366
        >>> airplane.miles
        45267.7
        """

        self.model = plane_model
        self.serial = serial_num 
        self.seats = num_seats
        self.miles = miles_travelled

    def log_trip(self, num_miles):
        """ (Airplane, float) -> NoneType

        Precondition: num_miles > 0.0

        Record that the airplane travelled num_miles additional miles.

        >>> airplane = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> airplane.log_trip(1000.0)
        >>> airplane.miles
        46267.7
        """

        self.miles += num_miles 

    def __eq__(self, other):
        """(Airplane, Airplane) -> bool

        Return whether this Airplane has the same numbers as other.

        >>> a1 = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> a2 = Airplane('Boeing 747', '48955', 366, 45267.7)
        >>> a3 = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> a1 == a2
        False
        >>> a1 == a3
        True
        """

        return self.serial == other.serial

    def __str__(self):
        """(Information) -> str

        Return a string representation of this information.
        """

        information = 'Airplane({}, {}, {}, {})'.format(self.model, self.serial, self.seats, self.miles)

        return information 

class Flight:
    """ Information about an airplane flight. """

    def __init__(self, plane):
        """ (Flight, Airplane) -> NoneType
        Create a Flight with an empty passenger list on airplane plane.
        >>> a = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> f = Flight(a)
        >>> str(f.airplane)
        'Airplane(Boeing 747, 19643, 366, 45267.7)'
        >>> f.passengers
        []
        """

        self.airplane = plane
        self.passengers = []

    def add(self, passenger):
        """ (Flight, str) -> bool
        If there are still seats available on this flight, add passenger to the
        passenger list. Return True iff passenger is added to this flight.
        >>> a = Airplane('Cessna 150E', '9378', 1, 824.8)
        >>> f = Flight(a)
        >>> f.add('Myrto')
        True
        >>> f.add('Jen')
        False
        """
        
        if len(self.passengers) + 1 <= self.airplane.seats:
            self.passengers.append(passenger)         
            return True 
        else:
            return False 

    def change_planes(self, other_airplane):
        """ (Airplane) -> int

        If other_airplane has enough seats to hold the passengers on this flight,
        use other_airplane for this flight. Whether or not we change to other_airplane,
        return the number of available seats on this flight (seats not currently occupied
        by passengers).

        >>> a1 = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> f = Flight(a1)
        >>> f.add('Myrto')
        True
        >>> f.add('Jen')
        True
        >>> a2 = Airplane('Bombardier Dash 8', '11234', 39, 6444.6)
        >>> f.change_planes(a2)
        37
        >>> a3 = Airplane('Cessna 150E', '9378', 1, 824.8)
        >>> f.change_planes(a3)
        0
        """

        if len(self.passengers) + 1 <= other_airplane.seats:
            self.airplane = other_airplane
            x = self.airplane.seats - len(self.passengers) 
            return x 
        else:
            return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()






