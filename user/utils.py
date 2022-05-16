from utils import get_posts_all
from config import POSTS_PATH


def get_posts_by_user(user_name):
    """
    Поиск постов определённого пользователя
    :param user_name: Имя пользователя
    :return: Список постов
    """
    posts = get_posts_all(POSTS_PATH)
    user_posts = []
    for post in posts:
        if post["poster_name"] == user_name:
            user_posts.append(post)

    return user_posts
