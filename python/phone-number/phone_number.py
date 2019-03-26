import re

class Phone(object):
    def __init__(self, phone_number):
        self.number = phone_number

        self.extract(phone_number)
        self.validate()
        self.populate()

    def extract(self, number):
        """ extract the phone number """

        # regular expressions to run through
        self.regexps = [
            re.compile(r'1(\d{10})'),
            re.compile(r'\((\d{3})\) (\d{3})\-(\d{4})'),
            re.compile(r'(\d+)\.(\d+)\.(\d+)'),
            re.compile(r'(\d+)\s*(\d+)\s*(\d+)\s*'),
        ]

        for regex in self.regexps:
            hit = regex.search(number)
            if hit:
                self.number = "".join(hit.groups())
                return
        raise ValueError("Could not find phone number")

    def validate(self):
        """ validate the phone number format"""

        n = self.number
        if len(n) != 10:
            raise ValueError("Not enough digits")

        if (n[0] == '0') or (n[0] == '1'):
            raise ValueError("Invalid area code")

        if (n[3] == '0') or (n[3] == '1'):
            raise ValueError("Invalid exchange code")
        return True

    def populate(self):
        """ once extracted, validated, populate fields """
        self.area_code = self.number[0:3]

    def pretty(self):
        """ pretty-print"""

        area = self.number[0:3]
        exch = self.number[3:6]
        rest = self.number[6:]
        return f'({area}) {exch}-{rest}'

