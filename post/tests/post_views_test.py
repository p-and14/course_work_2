from main import app
import json

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_post_status():
    response = app.test_client().get('/posts/1', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса поста не ок"


def test_posts_json():
    response = app.test_client().get('/api/posts/1')
    data = response.json
    assert type(data) == dict, "Возвращается не словарь"
    assert set(data.keys()) == keys_should_be, "Неверный список ключей"
