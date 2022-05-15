from feed.dao.feed_dao import FeedDAO
import pytest
from config import POSTS_PATH


@pytest.fixture()
def feed_dao():
    posts_dao_instance = FeedDAO(POSTS_PATH)
    return posts_dao_instance


keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestFeedDAO:

    def test_get_posts_all(self, feed_dao):
        posts = feed_dao.get_posts_all()
        assert type(posts) == list, "Возвращается не список"
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "Неверный список ключей"
