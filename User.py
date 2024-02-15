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

    def follow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        u1.followers.add(self)
        print(f"{self.username} started following {u1.username}")

    def unfollow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        u1.followers.remove(self)
        print(f"{self.username} unfollowed {u1.username}")

    def publish_post(self, *args):  # Factory method pattern
        """
         This function implements *observer design pattern* like "Subject" by : update function.
         it is responsible for updating all the "observers" about a new post.
         in our case the observers are the all users that following after post owner.

         This function implements *factory design pattern* the user put a parameters
         and the function responsible to create post by user wishes like factory
         """
        if args[0] == "Text":
            post_t = TextPost(self, args[0], args[1])
            self.posts.append(post_t)
            print(f'{self.username} published a post:\n"{args[1]}"\n')
            self.update(f"{self.username} has a new post")
            return post_t
        elif args[0] == "Image":
            post_img = ImagePost(self, args[0], args[1])
            self.posts.append(post_img)
            print(f"{self.username} posted a picture\n")
            self.update(f"{self.username} has a new post")
            return post_img
        elif args[0] == "Sale":
            post_sale = SalePost(self, args[0], args[1], args[2], args[3])
            self.posts.append(post_sale)
            print(f"{self.username} posted a product for sale:\n"
                  f"{post_sale.status} {args[1]}, price: {args[2]}, pickup from: {args[3]}\n")
            self.update(f"{self.username} has a new post")
            return post_sale

    def print_notifications(self):
        # for i in self.notifications:
        result = "\n".join(self.notifications)
        print(f"{self.username}'s notifications:\n{result}")

    def update(self, new_notification):
        for follower in self.followers:
            follower.notifications.append(new_notification)

    def __str__(self):
        all_users = (f"User name: {self.username}, Number of posts: {len(self.posts)},"
                     f" Number of followers: {len(self.followers)}")
        return all_users
