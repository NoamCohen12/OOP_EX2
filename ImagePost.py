from Post import Post
import matplotlib.pyplot as plt
from matplotlib import image


class ImagePost(Post):
    def __init__(self, user: "User", post_type, image_path):
        super().__init__(user, post_type)
        self.image_path = image_path

    def display(self):
        img = image.imread(self.image_path)
        plt.imshow(img)
        plt.show()
