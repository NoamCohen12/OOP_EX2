# from matplotlib import image as plt
from matplotlib import image, pyplot as plt


class Post:
    def __init__(self, post_owner, post_type):
        self.post_owner = post_owner
        self.post_type = post_type
        # it's set because every user can do only one like to each post
        self.likes_list = set()
        self.comment_list = dict()

    def like(self, u1):
        # user can't like himself post
        if u1.is_online:
            self.likes_list.add(u1)
            if self.post_owner != u1:
                self.notification_update(u1, "like")
        else:
            raise RuntimeError(f"The user: {u1.username} is not online")

    def comment(self, u2, text: "comment"):
        if u2.is_online:
            self.comment_list[u2] = text
            if self.post_owner != u2:
                self.notification_update(u2, "comment", text)
        else:
            raise RuntimeError(f"The user: {u2.username} is not online")

    def notification_update(self, user, *args):
        """
        This function implements observer design pattern like "Subject"
        it is responsible for updating all the "observers" likes and comments and a new post
        we have different case :
        first someone liked or commented on user post than he gets notification on it
        second user create a new post than the function send notification to all his followers.
        """

        if self.post_owner.username != user.username:  # if I am the "post owner" I don't want to update myself
            if args[0] == "like":
                print(f"notification to {self.post_owner.username}: {user.username} liked your post")
                self.post_owner.notifications.append(f"{user.username} liked your post")
            if args[0] == "comment":
                self.post_owner.notifications.append(f"{user.username} commented on your post")
                print(f"notification to {self.post_owner.username}: {user.username} commented on your post: {args[1]}")
        if args[0] == "post":
            user.update(f"{self.post_owner.username} has a new post")


class TextPost(Post):
    """
        Represents a text-based post on a social networking platform.
        Subclass of Post.
        """
    def __init__(self, post_owner, post_type, text):
        super().__init__(post_owner, post_type)
        self.text = text

    def __str__(self):
        """
         Return a string representation of the TextPost instance.
         """
        return f'{self.post_owner.username} published a post:\n"{self.text}"\n'


class SalePost(Post):
    """
      Represents a post for selling items on a social networking platform.
      Subclass of Post.
      """
    def __init__(self, post_owner, post_type, description, price, location):
        super().__init__(post_owner, post_type)
        self.description = description
        self.price = price
        self.location = location
        self.status = "For sale!"

    def discount(self, percent_discount, password: str):
        if password == self.post_owner.password:
            self.price = self.price * (1 - (percent_discount / 100))
            print(f"Discount on {self.post_owner.username} product! the new price is: {self.price}")

    def sold(self, password: str):
        if password == self.post_owner.password:
            self.status = "Sold!"
            print(f"{self.post_owner.username}'s product is sold")

    def __str__(self):
        """
        Return a string representation of the SalePost instance.
        """
        return (f"{self.post_owner.username} posted a product for sale:\n"
                f"{self.status} {self.description}, price: {self.price}, pickup from: {self.location}\n")


class ImagePost(Post):
    """
       Represents an image-based post on a social networking platform.
       Subclass of Post.
       """
    def __init__(self, post_owner, post_type, image_path):
        super().__init__(post_owner, post_type)
        self.image_path = image_path

    def display(self):
        img = image.imread(self.image_path)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        """
         Return a string representation of the ImagePost instance.
          """
        return f"{self.post_owner.username} posted a picture\n"
