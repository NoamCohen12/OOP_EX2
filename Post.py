# from User import User
import matplotlib.pyplot as plt
from matplotlib import image


class Post:
    def __init__(self, user, post_type):
        self.user = user
        self.post_type = post_type
        self.likes_list = set()
        self.comment_list = dict()

    def like(self, u1):
        self.likes_list.add(u1)

    def comment(self, u2, text: "comment"):
        self.comment_list[u2] = text

    # def __str__(self):
    #     if self.post_type == "Sale":
    #         SalePost.__str__(Post)
    #
    #     elif self.post_type == "Text":
    #
    #     elif self.post_type == "Image":


class TextPost(Post):
    def __init__(self, user, post_type, text):
        super().__init__(user, post_type)
        self.text = text

    def __str__(self):
        return f'{self.user.username} published a post:\n"{self.text}"\n'


class SalePost(Post):
    def __init__(self, user, post_type, description, price, location):
        super().__init__(user, post_type)
        self.description = description
        self.price = price
        self.location = location
        self.status = "For sale!"

    def discount(self, percent_discount, password: str):
        if password == self.user.password:
            self.price = self.price * (1 - (percent_discount / 10))
            print(f"Discount on {self.user.username} product! the new price is: {self.price}")

    def sold(self, password: str):
        if password == self.user.password:
            self.status = "Sold!"
            print(f"{self.user.username} product is sold")

    def __str__(self):
        return (f"{self.user.username} posted a product for sale:\n"
                f"{self.status} {self.description},price: {self.price},pickup from: {self.location}")


class ImagePost(Post):
    def __init__(self, user, post_type, image_path):
        super().__init__(user, post_type)
        self.image_path = image_path

    def display(self):
        pass
        # img = image.imread(self.image_path)
        # plt.imshow(img)
        # plt.show()

    def __str__(self):
        return f"{self.user.username} published a picture"
