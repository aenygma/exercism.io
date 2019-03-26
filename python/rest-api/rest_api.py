import json
from pprint import pprint as pp

class DB(object):

    def __init__(self, db):
        self.db = db

    def get_users(self):
        return self.db.get('users')

    def get_usernames(self):
        """ get usernames """

        return [i.get('name') for i in self.get_users()]

    def get_usersinfo(self, names=[]):
        """ get user/s info """
        assert isinstance(names, list), "names must be a list"

        ret = []
        if names is []:
            return self.get_users()

        for name in names:
            for user in self.get_users():
                if user.get('name') == name:
                    ret.append(user)
        return ret

    def add_user(self, name):
        """ create new user """

        # validate no entry exists
        if name in self.get_usernames():
            return self.get_usersinfo([name])

        new_user = {
            'name': f'{name}',
            'owes': {},
            'owed_by': {},
            'balance': 0}
        self.get_users().append(new_user)
        return new_user

    def transaction(self, lender, borrower, amount):
        """ process transactions """

        # get users' info
        luser = self.get_usersinfo(names=[lender])
        buser = self.get_usersinfo(names=[borrower])

        if (len(luser) != 1) or (len(buser) != 1):
            raise Exception("Non-unique or no user found", lender, borrower)

        luser, buser = luser[0], buser[0]

        # only use "owes", 
        lender_owes = luser["owes"].get(borrower, 0)
        borrower_owes = buser["owes"].get(lender, 0)

        # if pre-existing account exists
        lender_owes = lender_owes - amount

        # if outstanding, update lender's debt, clear borrower debt (if any)
        if lender_owes > 0:
            luser["owes"].update({borrower: lender_owes})
            buser["owes"].pop(lender, None)

            # update otherside
            buser["owed_by"].update({lender:  lender_owes})
            luser["owed_by"].pop(lender, None)
        # if overpaid, update borrower "owes", clear lender debt (if any)
        elif lender_owes < 0:
            buser["owes"].update({lender: -1*lender_owes})
            luser["owes"].pop(borrower, None)

            # update otherside
            luser["owed_by"].update({borrower: -1*lender_owes})
            buser["owed_by"].pop(lender, None)
        else:
            luser["owes"].pop(borrower, None)
            buser["owes"].pop(lender, None)

            # update otherside
            luser["owed_by"].pop(borrower, None)
            buser["owed_by"].pop(lender, None)

        # update balance
        luser['balance'] = luser.get('balance') + amount
        buser['balance'] = buser.get('balance') - amount

        return self.get_usersinfo(names=[lender, borrower])

class RestAPI(object):

    def __init__(self, database=None):
        self.db = DB(database)

    def get(self, url, payload="{}"):
        """ service a get request"""

        ret = {}
        data = json.loads(payload)

        if url == '/users':
            ret = self.db.get_usersinfo(data.get("users", []))
            ret = {"users": ret}

        return json.dumps(ret)

    def post(self, url, payload={}):
        """service a post request"""

        ret = {}
        data = json.loads(payload)

        if url == '/add':
            ret = self.db.add_user(data.get("user"))

        elif url == '/iou':
            ret = self.db.transaction(**data)
            ret.sort(key = lambda x: x.get('name'))
            ret = {"users": ret}

        return json.dumps(ret)


