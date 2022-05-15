from search.utils import search_for_posts

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_search_for_posts():
    posts_with_query = search_for_posts("Ага, опять еда!")
    assert posts_with_query[0]["pk"] == 1, "Возвращаются неправильные посты"
    assert set(posts_with_query[0].keys()) == keys_should_be, "Неверный список ключей"
