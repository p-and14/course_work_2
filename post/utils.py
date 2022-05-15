from utils import get_posts_all, get_comments_all
from config import POSTS_PATH, COMMENTS_PATH


def get_post_by_pk(pk):
    """

    :param pk:
    :return:
    """
    posts = get_posts_all(POSTS_PATH)

    for post in posts:
        if post["pk"] == int(pk):
            return post


def get_comments_by_post_id(post_id):
    comments_all = get_comments_all(COMMENTS_PATH)
    comments_by_post_id = []
    for comment in comments_all:
        if comment["post_id"] == int(post_id):
            comments_by_post_id.append(comment)

    return comments_by_post_id
