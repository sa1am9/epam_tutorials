import datetime
import uuid


class RegularTicket:

    def __init__(self):
        self.key = str(uuid.uuid4())
        self.price = 100
        self.date = None

    def __str__(self):
        return "type: Regular, price - {}, key - {}".format(self.price,
                                                            self.key)

    def get_price(self):
        return self.price

    def props(cls):
        return [i for i in cls.__dict__.keys() if i[:1] != '_']

    """
    Confused
    """
    def __get__(self, instance, owner):
        pass


class AdvanceTicket(RegularTicket):
    def __init__(self):
        super().__init__()
        self.price *= 1
        self.price *= 0.4

    def __str__(self):
        return "type: Advance, price - {}, key - {}".format(self.price,
                                                            self.key)


class LateTickets(RegularTicket):

    def __init__(self):
        super().__init__()
        self.price *= 1
        self.price *= 0.1

    def __str__(self):
        return "type: Late, price - {}, key - {}".format(self.price,
                                                            self.key)


class StudentTickets(RegularTicket):

    def __init__(self):
        super().__init__()
        self.price *= 1
        self.price *= 0.5

    def __str__(self):
        return "type: Student, price - {}, key - {}".format(self.price,
                                                            self.key)


if __name__ == "__main__":

    date = int(input("How many days to ivent? \n"))
    if date < 60:
        pass
    if date > 10:
        pass
    """
    Invented an implementation on time, but too little time left.
    """
    s = RegularTicket()
    print(s)
    print(s.get_price())

    s = StudentTickets()
    print(s)
    print(s.get_price())

    s = LateTickets()
    print(s)
    print(s.get_price())

    s = AdvanceTicket()
    print(s)
    print(s.get_price())
