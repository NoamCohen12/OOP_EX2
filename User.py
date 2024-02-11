# from ImagePost import ImagePost
from Post import SalePost, TextPost, ImagePost


# from SalePost import SalePost
# from TextPost import TextPost


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.posts = []

    def follow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        u1.followers.add(self.username)
        print(f"{self.username} started following {u1.username}")

    def unfollow(self, u1: "User"):
        # because it's set we don't need to check if the followers was in the set
        u1.followers.remove(self.username)
        print(f"{self.username} unfollowed {u1.username}")

    def publish_post(self, *args):
        if args[0] == "Text":
            post_t = TextPost(self, args[0], args[1])
            self.posts.append(post_t)
            print(f'{self.username} published a post:\n"{args[1]}"\n')
            return post_t
        elif args[0] == "Image":
            post_img = ImagePost(self, args[0], args[1])
            self.posts.append(post_img)
            print(f"{self.username} posted a picture\n")
            return post_img
        elif args[0] == "Sale":
            post_sale = SalePost(self, args[0], args[1], args[2], args[3])
            self.posts.append(post_sale)
            print(f"{self.username} posted a product for sale:\n"
                  f"{post_sale.status} {args[1]}, price: {args[2]}, pickup from: {args[3]}\n")
            return post_sale

    def __str__(self):
        all_users = (f"User name: {self.username}, Number of posts: {len(self.posts)},"
                     f" Number of followers: {len(self.followers)}")
        return all_users
