from datetime import datetime

class UserProfile:
    def __init__(self, username, password, email, profile_picture=None):
        self.username = username
        self.password = password
        self.email = email
        self.profile_picture = profile_picture
        self.friends = []
        self.chats = []

    def add_friend(self, username):
        if username not in self.friends:
            self.friends.append(username)
            return True
        else:
            return False

    def remove_friend(self, username):
        if username in self.friends:
            self.friends.remove(username)
            return True
        else:
            return False

    def add_chat(self, chat):
        if chat in self.chats:
            return False
        else:
            self.chats.append(chat)
            return True
        
    def remove_chat(self, chat):
        if chat in self.chats:
            self.chats.remove(chat)

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Friends: {', '.join(self.friends)}, Chats: {len(self.chats)}"

    def getUsername():
        return self.username

    def getEmail():
        return self.email

    def getFriendList():
        return self.friends

    def getChats():
        return self.chats

    def getChat(receiver):
        for chat in self.chats:
            if chat.getUser2() == receiver:
                return chat
            
            
            
class Chat:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def __str__(self):
        return f"Chat between {self.user1.username} and {self.user2.username}, Messages: {len(self.messages)}"

    def getUser2():
        return self.user2

    def getUser1():
        return self.user1

    def getMessages():
        return self.messages


class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        current_datetime = datetime.now()
        self.date = current_datetime.strftime("%Y-%m-%d")
        self.time = current_datetime.strftime("%H:%M:%S")

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_content(self):
        return self.content

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

