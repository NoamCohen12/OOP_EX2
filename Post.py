from User import User


class Post:
    def __init__(self, post_type):
        self.post_type = post_type
        self.likes_list = set()
        self.comment_list = dict()

    def like(self, u1: "User"):
        self.likes_list.add(u1)

    def comment(self, u2: "User", text: "comment"):
        self.comment_list[u2] = text

    def publish_post(self):
        if
