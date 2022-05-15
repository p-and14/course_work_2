from main import app


def test_tag_status():
    response = app.test_client().get('/tag/кот', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса закладок не ок"
