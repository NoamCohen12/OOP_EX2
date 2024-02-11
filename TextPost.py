from Post import Post


class TextPost(Post):
    def __init__(self, user: "User", post_type, text):
        super().__init__(user, post_type)
        self.text = text
