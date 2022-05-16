import json


class FeedDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """
        Загружает посты из файла
        :return: Список постов
        """
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)

        return posts

    def get_posts_all(self):
        """
        Получает список всех постов
        :return: Список всех постов
        """
        return self.load_data()
