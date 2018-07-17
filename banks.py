from datetime import datetime

class Bank(object):
    def __init__(self, number, type):

        self.__number = str(number)
        self.__type = type
        self.__out = False
        self.__signed_in = True
        self.__out_log = {}
        self.__out_info = {}
        self.__returned = True
        self.__made = True             #check if the bank was made, also how much money was put in, update signout to make sure its made
        self.__amount = "0"
        self.__notes = ""

    def number(self):
        return self.__number

    def banktype(self):
        return self.__type

    def out(self):
        return self.__out

    def signed_in(self):
        return self.__signed_in

    def returned(self):
        return self.__returned

    def made(self):
        return self.__made

    def amount(self):
        return self.__amount

    def notes(self):
        return self.__notes

    def signoutinfo(self):
        return self.__out_info

    def signoutlog(self):
        return self.__out_log

    def signout(self, name, location, notes):
        if not self.__out and self.__signed_in and self.__returned and self.__made:
            self.__out = True
            self.__signed_in = False
            self.__returned = False
            self.__made = False
            self.__notes = notes
            self.__out_info = {"Name_Out":name, "Location":location, "Amount":self.__amount, "Time_Out":datetime.now(), "Returned":self.__returned}
            if self.__notes != "":
                self.__out_info["Notes"] = self.__notes

        else:
            print("That bank is already out")

    def signin(self, name):
        if self.__out and not self.__signed_in and not self.__returned:
            self.__signed_in = True
            self.__out_info["Name_In"] = name
            self.__out_info["Time_In"] = datetime.now()

    def returnbank(self):
        if self.__out and self.__signed_in and not self.__returned:
            self.__returned = True
            self.__out = False
            self.__out_info["Returned"] = self.__returned
            self.__out_log["{}/{}/{} {}:{}".format(datetime.now().month, datetime.now().day, datetime.now().year, datetime.now().hour, datetime.now().minute)] = self.__out_info

    def makebank(self, amount):
        if self.__returned and not self.__made:
            self.__amount = str(amount)
            self.__made = True

    def __str__(self):
        return "{} #{}".format(self.__type, self.__number)



class Bar(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "bar"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")


    def __str__(self):
        return "Bar Bank object"

class FB(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "fb"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "FB Bank object"

class TKG(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "tkg"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "TKG Bank object"

class Retail(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "retail"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "Retail Bank object"



class Bike(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "bike"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "Bike Bank object"


class Change(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "change"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "500"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "Change Bank object"


class Fanny(object):

    def __init__(self):

        self.__banks = []

    def addbank(self, number):
        """Adds a new bank to the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                print("Bank already exists")
        if not found:
            self.__banks.append(Bank(number, "fanny"))

    def removebank(self, number):
        """Removes a bank from the list"""
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                self.__banks.remove(bank)
        if not found:
            print("Bank not found")

    def banks(self):
        """Returns the list of banks"""
        return self.__banks

    def signout(self, name, location, number, notes = ""):
        """
        Signs out a bank
        name = person signing out
        location = the location the person is bringing the bank
        number = bank number being taken
        notes = any special information needed at the time of sign out
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if not bank.out() and bank.signed_in() and bank.returned():
                    bank.signout(name, location, notes)
                elif bank.out():
                    print("Bank is out")
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif not bank.returned():
                    print("Bank not returned")
        if not found:
            print("Bank not found")

    def signedout(self):
        """Returns a list of all banks currently out"""
        out = []
        for bank in self.__banks:
            if bank.out():
                out.append(bank)
        return out

    def signin(self, name, number):
        """
        Signs a bank back in
        name = person signing it in
        number = bank being signed in
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.out() and not bank.signed_in() and not bank.returned():
                    bank.signin(name)
                elif not bank.out():
                    print("Bank is not out")
                elif bank.signed_in():
                    print("Bank signed in")
                elif bank.returned():
                    print("Bank already returned")
        if not found:
            print("Bank not found")

    def signedin(self):
        """Returns a list of banks that have been signed in"""
        signin = []
        for bank in self.__banks:
            if bank.signed_in():
                signin.append(bank)
        return signin

    def returnbank(self, number):
        """
        Mark a bank returned
        number = bank being marked
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.signed_in() and not bank.returned() and bank.out():
                    bank.returnbank()
                elif not bank.signed_in():
                    print("Bank not signed in")
                elif bank.returned():
                    print("Bank already returned")
                elif not bank.out():
                    print("Bank is not out")
        if not found:
            print("Bank not found")

    def returnedbanks(self):
        """
        List of banks that have been returned
        """
        returned = []
        for bank in self.__banks:
            if bank.returned():
                returned.append(bank)
        return returned

    def makebank(self, number, amount = "350"):
        """
        Makes a bank, i.e. the bank is prepared and ready to be signed out
        number = bank being made
        amount = how much money put into the bank
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                if bank.returned() and not bank.made():
                    bank.makebank(amount)
                elif not bank.returned():
                    print("Bank not returned")
                elif bank.made():
                    print("Bank already made")
        if not found:
            print("Bank not found")

    def madebanks(self):
        """
        Returns a list of banks that are made and ready to be signed out
        """
        made = []
        for bank in self.__banks:
            if bank.made():
                made.append(bank)
        return made

    def get_notes(self, number):
        """
        Returns the notes for a given bank
        number = bank number of notes wanted
        """
        found = False
        for bank in self.__banks:
            if bank.number() == str(number):
                found = True
                return bank.notes()
        if not found:
            print("Bank not found")

    def __str__(self):
        return "Fanny Bank object"
