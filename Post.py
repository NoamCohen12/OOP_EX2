from User import User


class Post:
    def __init__(self, user: "User", post_type):
        self.user = user
        self.post_type = post_type
        self.likes_list = set()
        self.comment_list = dict()

    def like(self, u1: "User"):
        self.likes_list.add(u1)

    def comment(self, u2: "User", text: "comment"):
        self.comment_list[u2] = text


def __str__(self):
    if self.post_type == "Sale":
        print(f"{self.username} posted a product for sale:\n"
              f"{self.status}{self.description},price: {self.price},pickup from: {self.location}")
    elif self.post_type == "Text":
        print(f'{self.username} published a post:\n"{self.text}"')
    elif self.post_type == "Image":
        print(f"{self.username} published a picture")
