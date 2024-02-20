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
        if 4 <= len(password) <= 8:
            u1 = User(username, password)
            if u1.username not in self.users:
                self.users[u1.username] = u1
                u1.is_online = True
                return u1
        else:
            raise print("illegal password")

    # ---------------------------------------------------------------------------------------------
    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.users[username].is_online = True
            print(f"{username} connected")

    # ---------------------------------------------------------------------------------------------
    def log_out(self, username):
        if username in self.users:
            self.users[username].is_online = False
            print(f"{username} disconnected")

    # ---------------------------------------------------------------------------------------------

    def __str__(self):
        """
        Return a string representation of the SocialNetwork instance.
         """
        all_users = ""
        # for index, user in enumerate(self.users.values()):
        #     all_users += str(user)
        #     if index != len(self.users) + 2:  # Check if it's not the last user
        #         all_users += "\n"
        for user in self.users.values():
            all_users += str(user) + "\n"
        all_users = f"{self.name} social network:\n" + all_users
        all_users = all_users[:-1]
        return all_users
