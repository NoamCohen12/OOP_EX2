from User import User


class SocialNetwork:

    def __init__(self, name):
        self.name = name
        self.users = {}
        print(f"The social network {name} was created!")

    def sign_up(self, username, password):
        u1 = User(username, password)

        if u1.username not in self.users:
            self.users[u1.username] = u1
