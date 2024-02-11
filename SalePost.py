from Post import Post
from User import User


class SalePost(Post):
    def __init__(self, user: "User",post_type, description, price, location):
        super().__init__(user, post_type)
        self.description = description
        self.price = price
        self.location = location




       def discount(self, percent_discount , password:str):
           if password == self.user.password:
               self.price = self.price *(1-(percent_discount/10))
               print(f"Discount on {self.user.username} product! the new price is: {self.price}")




