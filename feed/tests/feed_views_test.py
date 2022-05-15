from main import app

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_feed_status():
    response = app.test_client().get('/', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса кандидатов не ок"


def test_posts_json():
    response = app.test_client().get('/api/posts')
    data = response.json
    assert type(data) == list, "Возвращается не список"
    assert set(data[0].keys()) == keys_should_be, "Неверный список ключей"
