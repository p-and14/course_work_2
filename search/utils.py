from utils import get_posts_all
from config import POSTS_PATH


def search_for_posts(query):
    """
    Поиск постов по ключевому слову
    :param query: Ключевое слово для поиска
    :return: Список постов
    """
    posts = get_posts_all(POSTS_PATH)
    posts_with_query = []
    if query:
        query = query.lower()

    for post in posts:
        if query in post["content"].lower():
            posts_with_query.append(post)

    return posts_with_query
