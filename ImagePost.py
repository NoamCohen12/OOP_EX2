from Post import Post


class ImagePost(Post):
    def __init__(self, post_type, image_path):
        self.post_type = post_type
        self.image_path = image_path

    def publish_post(self):