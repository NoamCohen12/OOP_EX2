from User import User

"""
 This function implements *Singleton design pattern*. 
 during the entire run only one instance will be created.
 thanks to the flags "__instance" and "__is_init".
 also The conditions on the creation functions :"__new__" and "__init__" of the SocialNetwork.
 
 
         
"""


class SocialNetwork:  # Singleton Design Pattern
    __instance = None  # Class variable to store the single instance
    __is_init = False  # Flag to track initialization status

    def __new__(cls, name):
        # Create a new instance only if no instance exists
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Create new instance
        return cls.__instance  # Return existing or newly created instance

    def __init__(self, name):
        if self.__is_init:
            return  # If instance is already initialized, exit initialization ,else Initialize it with new values
        self.name = name
        self.users = {}
        self.__is_init = True
        print(f"The social network {self.name} was created!")

    def sign_up(self, username, password):
        u1 = User(username, password)

        if u1.username not in self.users:
            self.users[u1.username] = u1
            return u1

    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"{username} connect")

    def log_out(self, username):
        print(f"{username} disconnect")

    def __str__(self):
        all_users = ""
        for user in self.users.values():
            all_users += str(user) + "\n"

        return f"{self.name} social network:\n{all_users}"
        # return user.__str__()
