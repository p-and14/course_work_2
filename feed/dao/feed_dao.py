import json


class FeedDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """

        :return:
        """
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)

        return posts

    def get_posts_all(self):
        """

        :return:
        """
        return self.load_data()
