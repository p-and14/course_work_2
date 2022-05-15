from user.utils import get_posts_by_user

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_posts_by_user():
    posts_by_user = get_posts_by_user("leo")
    assert posts_by_user[0]["poster_name"] == "leo", "Возвращаются неправильные посты"
    assert set(posts_by_user[0].keys()) == keys_should_be, "Неверный список ключей"
