class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()

        def add_follower(u1: "User"):
            # because it's set we don't need to check if the followers was in the set
            self.followers.add(username)
            print(f"{u1.username} started following {username}")

        def publish_post(u1:"")
