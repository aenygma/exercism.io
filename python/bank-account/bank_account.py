from threading import Lock

class BankAccount(object):
    def __init__(self):
        self.active = False
        self.balance = 0
        self._lock = Lock()

    def _validate_open(self):
        if not self.active:
            raise ValueError("Account not open")

    def get_balance(self):
        """ get current balance """

        self._validate_open()
        return self.balance

    def open(self):
        """ open account """

        if self.active:
            raise ValueError("Account already open")
        self.active = True

    def deposit(self, amount):
        """ deposit amount """

        self._validate_open()
        if amount < 0:
            raise ValueError("Deposits cannot be negative")
        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        """ withdraw amount """

        self._validate_open()
        if amount < 0:
            raise ValueError("Withdrawl cannot be negative")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")
        with self._lock:
            self.balance -= amount

    def close(self):
        """ close account """

        self._validate_open()
        self.active = False
        self.balance = 0

