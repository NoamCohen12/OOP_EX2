from Post import Post
from User import User


class ImagePost(Post):
    def __init__(self,user: "User", post_type, image_path):
        super().__init__(user, post_type)
        self.image_path = image_path

