import json
from post.utils import get_post_by_pk
from config import BOOKMARKS_PATH


def get_bookmarks():
    with open(BOOKMARKS_PATH, "r", encoding="utf-8") as file:
        bookmarks = json.load(file)

    return bookmarks


def add_bookmark(post_id):
    post = get_post_by_pk(post_id)
    bookmarks = get_bookmarks()
    if post not in bookmarks:
        bookmarks.append(post)
        with open(BOOKMARKS_PATH, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, indent=2, ensure_ascii=False)


def remove_bookmark(post_id):
    post = get_post_by_pk(post_id)
    bookmarks = get_bookmarks()
    if post in bookmarks:
        bookmarks.remove(post)
        with open(BOOKMARKS_PATH, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, indent=2, ensure_ascii=False)
