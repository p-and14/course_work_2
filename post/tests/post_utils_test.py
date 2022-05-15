from post.utils import get_post_by_pk

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_post_by_pk():
    post_by_pk = get_post_by_pk(1)
    assert post_by_pk["pk"] == 1, "Возвращается неправильный пост"
    assert set(post_by_pk.keys()) == keys_should_be, "Неверный список ключей"
