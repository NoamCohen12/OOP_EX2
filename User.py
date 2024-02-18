from Post import SalePost, TextPost, ImagePost


class Observer:
    notifications = []

    def update(self, *args):
        pass


"""
this class implements *observer design pattern* User want to get notification 
and therefore he inherits from "Observer"
"""


class User(Observer):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.posts = []
        self.notifications = []
        self.is_online = False

    def follow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        if self.is_online:
            u1.followers.add(self)
            print(f"{self.username} started following {u1.username}")

    def unfollow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        if self.is_online:
            u1.followers.remove(self)
            print(f"{self.username} unfollowed {u1.username}")

    def publish_post(self, *args):  # Factory method pattern
        """
         This function implements *factory design pattern* the user put a parameters
         and the function responsible to create post by user wishes (*args)like factory
         """
        if self.is_online:
            if args[0] == "Text":
                post_t = TextPost(self, args[0], args[1])
                self.posts.append(post_t)
                print(f'{self.username} published a post:\n"{args[1]}"\n')
                post_t.notification_update(post_t.post_owner, "post")
                return post_t
            elif args[0] == "Image":
                post_img = ImagePost(self, args[0], args[1])
                self.posts.append(post_img)
                print(f"{self.username} posted a picture\n")
                post_img.notification_update(post_img.post_owner, "post")
                return post_img
            elif args[0] == "Sale":
                post_sale = SalePost(self, args[0], args[1], args[2], args[3])
                self.posts.append(post_sale)
                print(f"{self.username} posted a product for sale:\n"
                    f"{post_sale.status} {args[1]}, price: {args[2]}, pickup from: {args[3]}\n")
                post_sale.notification_update(post_sale.post_owner, "post")
                return post_sale

    def print_notifications(self):
        """
       Print notifications received by the user.
         """
        result = "\n".join(self.notifications)
        print(f"{self.username}'s notifications:\n{result}")

    def update(self, new_notification: str):
        """
         Update method called by subjects to notify this user of new notifications.
          Parameters:
          new_notification (str): The new notification received.
          """
        for follower in self.followers:
            follower.notifications.append(new_notification)

    def __str__(self):
        """
         Return a string representation of the User instance.
        """
        user_description = (f"User name: {self.username}, Number of posts: {len(self.posts)},"
                            f" Number of followers: {len(self.followers)}")
        return user_description
