from utils import get_posts_all, get_comments_all
from config import POSTS_PATH, COMMENTS_PATH


def get_post_by_pk(pk):
    """
    Получает пост по номеру
    :param pk: Номер поста
    :return: Возвращает пост ввиде словаря
             Если пост не найден, то возвращает исключение TypeError
    """
    posts = get_posts_all(POSTS_PATH)

    for post in posts:
        if post["pk"] == int(pk):
            return post
    raise TypeError("Ошибка получения поста")


def get_comments_by_post_id(post_id):
    """
    Получает комментария к посту по номеру поста
    :param post_id: Номер поста
    :return: Список комментариев
    """
    comments_all = get_comments_all(COMMENTS_PATH)
    comments_by_post_id = []
    for comment in comments_all:
        if comment["post_id"] == int(post_id):
            comments_by_post_id.append(comment)

    return comments_by_post_id
