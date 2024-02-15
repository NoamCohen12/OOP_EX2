# matplotlib.pyplot as plt
from matplotlib import image


class Post:
    def __init__(self, post_owner, post_type):
        self.post_owner = post_owner
        self.post_type = post_type
        self.likes_list = set()
        self.comment_list = dict()

    def like(self, u1):
        self.likes_list.add(u1)
        self.update_likes_and_comments(u1, "like")
        # self.post_owner.update(f"{self.post_owner.username} liked your post")

    def comment(self, u2, text: "comment"):
        self.comment_list[u2] = text
        self.update_likes_and_comments(u2, "comment")
        # self.post_owner.update(f"{self.post_owner.username} commented on your post")

    def update_likes_and_comments(self, post_owner, type_of_notification: str):
        """
        This function implements observer design pattern like "Subject"
        it is responsible for updating all the "observers" Only likes and comments
        in our case the observ is the user who liked him
        """
        if self.post_owner.username != post_owner.username:
            if type_of_notification == "like":
                self.post_owner.notifications.append(f"{post_owner.username} liked your post")
            if type_of_notification == "comment":
                self.post_owner.notifications.append(f"{post_owner.username} commented on your post")


class TextPost(Post):
    def __init__(self, post_owner, post_type, text):
        super().__init__(post_owner, post_type)
        self.text = text

    def __str__(self):
        return f'{self.post_owner.username} published a post:\n"{self.text}"\n'


class SalePost(Post):
    def __init__(self, post_owner, post_type, description, price, location):
        super().__init__(post_owner, post_type)
        self.description = description
        self.price = price
        self.location = location
        self.status = "For sale!"

    def discount(self, percent_discount, password: str):
        if password == self.post_owner.password:
            self.price = self.price * (1 - (percent_discount / 10))
            print(f"Discount on {self.post_owner.username} product! the new price is: {self.price}")

    def sold(self, password: str):
        if password == self.post_owner.password:
            self.status = "Sold!"
            print(f"{self.post_owner.username} product is sold")

    def __str__(self):
        return (f"{self.post_owner.username} posted a product for sale:\n"
                f"{self.status} {self.description},price: {self.price},pickup from: {self.location}")


class ImagePost(Post):
    def __init__(self, post_owner, post_type, image_path):
        super().__init__(post_owner, post_type)
        self.image_path = image_path

    def display(self):
        pass
        # img = image.imread(self.image_path)
        # plt.imshow(img)
        # plt.show()

    def __str__(self):
        return f"{self.post_owner.username} published a picture\n"
