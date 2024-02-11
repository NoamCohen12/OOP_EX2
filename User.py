from ImagePost import ImagePost
from Post import Post
from SalePost import SalePost
from TextPost import TextPost


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.posts = []

        def add_follower(u1: "User"):
            # because it's set we don't need to check if the followers was in the set
            self.followers.add(username)
            print(f"{u1.username} started following {username}")

        def publish_post(*args):
            if args[0] == "Text":
                post_t = TextPost(self, args[0], args[1])
                self.posts.append(post_t)
                print(f"{self.username} published a post:\n{args[1]}")
                return post_t
            elif args[0] == "Image":
                post_img = ImagePost(self, args[0], args[1])
                self.posts.append(post_img)
                print(f"{self.username} posted a picture")
                return post_img
            elif args[0] == "Sale":
                post_sale = SalePost(self, args[0], args[1], args[2], args[3])
                self.posts.append(post_sale)
                print(f"{self.username} posted a product for sale:\n"
                      f"For sale! {args[1]}, price: {args[2]}, pickup from: {args[3]}")
                return post_sale
