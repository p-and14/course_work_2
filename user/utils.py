from utils import get_posts_all
from config import POSTS_PATH


def get_posts_by_user(user_name):
    """

    :param user_name:
    :return:
    """
    posts = get_posts_all(POSTS_PATH)
    user_posts = []
    for post in posts:
        if post["poster_name"] == user_name:
            user_posts.append(post)

    return user_posts
