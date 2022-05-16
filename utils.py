import json


def get_posts_all(path):
    """

    :return:
    """
    with open(path, "r", encoding="utf-8") as file:
        posts = json.load(file)

    return posts


def get_comments_all(path):
    """

    :param path:
    :return:
    """
    with open(path, "r", encoding="utf-8") as file:
        comments = json.load(file)

        return comments
