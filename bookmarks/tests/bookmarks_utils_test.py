from bookmarks.utils import get_bookmarks, add_bookmark, remove_bookmark

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_add_bookmark():
    add_bookmark(1)
    bookmarks = get_bookmarks()
    assert type(bookmarks) == list, "Возвращается не список"
    assert len(bookmarks) > 0, "Возвращается пустой список"
    assert set(bookmarks[-1].keys()) == keys_should_be, "Неверный список ключей"
    assert bookmarks[-1]["pk"] == 1, "Добавляется неверный пост"
    remove_bookmark(1)


def test_remove_bookmark():
    bookmarks = get_bookmarks()
    bookmarks_len = len(bookmarks)
    add_bookmark(2)
    remove_bookmark(2)
    bookmarks_after_remove = get_bookmarks()
    assert type(bookmarks) == list, "Возвращается не список"
    assert len(bookmarks_after_remove) <= bookmarks_len, "Удаление не работает"
