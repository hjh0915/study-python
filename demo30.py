class Member(object):
    """ A member of a university."""

    def __init__(self, name, address, email):
        """(Member, str, str, str) -> NoneType

        Create a new member named name, with home address and email address.
        """

        self.name = name 
        self.address = address
        self.email = email

class Faculty(Member):
    """ A faculty member at a university."""

    def __init__(self, name, address, email, faculty_num):
        """(Member, str, str, str) -> NoneType

        Create a new faculty named name, with home address, email address,
        faculty numberfaculty_num, and empty list of courses.
        """

        super(Faculty, self).__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

class Student(Member):
    """ A student member at a university."""

    def __init__(self, name, address, email, student_num):
        """(Member, str, str, str) -> NoneType

        Create a new student named name, with home address, email address,
        student number studen_num, an empty list of courses taken, and an 
        empty list of current courses.
        """

        super(Student, self).__init__(name, address, email)
        self.student_number = studen_num
        self.courses_taken = []
        self.courses_taking = []

    def __str__(self):
        """ (Member) -> str

        Return a string representaton of this Member.

        >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
        >>> member.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu'
        """

        return '{}\n{}\n{}'.format(self.name, self.address, self.email)


if __name__ == '__main__':
    paul = Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')

    print paul.name 
    print paul.email
    print paul.faculty_number

    print paul



    
