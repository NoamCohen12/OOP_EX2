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
            return u1

    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"{username} connect")

    def log_out(self, username):
        print(f"{username} disconnect")

    def __str__(self):
        all_users = ""
        for user in self.users.values():
            all_users += str(user)+"\n"

        return f"{self.name} social network:\n{all_users}"
         # return user.__str__()
