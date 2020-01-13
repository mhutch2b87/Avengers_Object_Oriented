# Using Visual Studio Code, Create an Object Oriented phone book that stores names, addresses and phone numbers of of avengers.
# Store each avenger name as a key and their information as values. Create a method that calls on a random avenger which should
# return their phone number

import random
from collections import defaultdict

#adding a name to phonebook
class Phonebook:

    def __init__(self, dict):
        self.dict = dict
    
    def addToPhonebook(self):
        name = input("please enter a name to add to phone book: ")
        phoneNumber = input("please enter {}'s phone number: ".format(name))
        address = input ("please enter {}'s Address: ".format(name))
        Lvalues =[phoneNumber, address]
        self.dict.setdefault(name, []).append(Lvalues)
        #example.setdefault('a', []).append('apple')
    def printPhoneBook(self):
        print(self.dict)
    
    def callRandom(self):
        choice = random.choice(list(self.dict.keys()))
        value = self.dict[choice][0]
        print(value)

Book1 = {}
phonebook = Phonebook(Book1)
while True:
    response = input("Would you like to Add, Random, or Quit: ")
    if response.lower() == 'add':
        phonebook.addToPhonebook()
        phonebook.printPhoneBook()
    elif response.lower() == 'random':
        phonebook.callRandom()
    else:
        break

