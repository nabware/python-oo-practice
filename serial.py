class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Initializes SerialGenerator object with start and current value """
        self.start = start
        self.next = self.start

    def generate(self):
        """ Increments current value by 1 and returns current value """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ Resets current value to start value """
        self.next = self.start
