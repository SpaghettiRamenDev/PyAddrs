class IP:
    class InvalidAddr(Exception):
        pass

    def __init__(self, ip=None):
        self.ip = ip or []

    def __getitem__(self, k):

        # User specified 0
        if k == 0:
            # Return a new object with the new value appended
            return IP(self.ip + ["0"])

        # User specified 1
        elif k == 1:
            # Return a new object with the new value appended
            return IP(self.ip + ["1"])

        # User specified 2
        elif k == 2:
            # Return a new object with the new value appended
            return IP(self.ip + ["2"])

        # User specified 3
        elif k == 3:
            # Return a new object with the new value appended
            return IP(self.ip + ["3"])

        # User specified 4
        elif k == 4:
            # Return a new object with the new value appended
            return IP(self.ip + ["4"])

        # User specified 5
        elif k == 5:
            # Return a new object with the new value appended
            return IP(self.ip + ["5"])

        # User specified 6
        elif k == 6:
            # Return a new object with the new value appended
            return IP(self.ip + ["6"])

        # User specified 7
        elif k == 7:
            # Return a new object with the new value appended
            return IP(self.ip + ["7"])

        # User specified 8
        elif k == 8:
            # Return a new object with the new value appended
            return IP(self.ip + ["8"])

        # User specified 9
        elif k == 9:
            # Return a new object with the new value appended
            return IP(self.ip + ["9"])

        # User specified 10
        elif k == 10:
            # Return a new object with the new value appended
            return IP(self.ip + ["A"])

        # User specified 11
        elif k == 11:
            # Return a new object with the new value appended
            return IP(self.ip + ["B"])

        # User specified 12
        elif k == 12:
            # Return a new object with the new value appended
            return IP(self.ip + ["C"])

        # User specified 13
        elif k == 13:
            # Return a new object with the new value appended
            return IP(self.ip + ["D"])

        # User specified 14
        elif k == 14:
            # Return a new object with the new value appended
            return IP(self.ip + ["E"])

        # User specified 15
        elif k == 15:
            # Return a new object with the new value appended
            return IP(self.ip + ["F"])

        # All other values are invalid
        else:
            # Raise an exception
            raise self.InvalidAddr("Invalid 4-bit value")

    def __str__(self):
        if len(self.ip) != 12:
            return "Bad IP"
        else:
            return (
                self.ip[0]
                + self.ip[1]
                + self.ip[2]
                + "."
                + self.ip[3]
                + self.ip[4]
                + self.ip[5]
                + "."
                + self.ip[6]
                + self.ip[7]
                + self.ip[8]
                + "."
                + self.ip[9]
                + self.ip[10]
                + self.ip[11]
            )
