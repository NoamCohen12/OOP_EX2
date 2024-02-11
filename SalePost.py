from Post import Post


class SalePost(Post):
    def __init__(self, post_type, description, price, location):
        super().__init__(post_type, description)
        self.post_type = post_type
        self.description = description
        self.price = price
        self.location = location
