from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chatmessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Rashmi', 'Ms.', 21, 4.5)

friend_one = Spy('Ruchi', 'Ms.', 21, 4.9)
friend_two = Spy('Munisha', 'Ms.', 23, 4.3)
friend_three = Spy('Satbir', 'Dr.', 22, 4.8)


friends = [friend_one, friend_two, friend_three]