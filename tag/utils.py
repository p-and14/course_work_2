from utils import get_posts_all
from config import POSTS_PATH


def get_posts_by_tag(tag_name):
    """
    Поиск постов по тэгу
    :param tag_name: Тэг-слово
    :return: Список постов
    """
    posts = get_posts_all(POSTS_PATH)
    posts_with_tag = []
    tag = f"#{tag_name}"
    for post in posts:
        if tag in post["content"]:
            posts_with_tag.append(post)

    return posts_with_tag
