from utils import get_posts_all, get_comments_all
from config import POSTS_PATH, COMMENTS_PATH

post_keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
comment_keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


def test_get_posts_all():
    posts = get_posts_all(POSTS_PATH)
    assert type(posts) == list, "Возвращается не список"
    assert len(posts) > 0, "Возвращается пустой список"
    assert set(posts[0].keys()) == post_keys_should_be, "Неверный список ключей"


def test_get_comments_all():
    posts = get_comments_all(COMMENTS_PATH)
    assert type(posts) == list, "Возвращается не список"
    assert len(posts) > 0, "Возвращается пустой список"
    assert set(posts[0].keys()) == comment_keys_should_be, "Неверный список ключей"
