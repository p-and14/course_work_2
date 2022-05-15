from main import app


def test_bookmarks_status():
    response = app.test_client().get('/bookmarks', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса закладок не ок"


def test_bookmark_add():
    response = app.test_client().get('/bookmarks/add/1', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса добавления закладок не ок"


def test_bookmark_remove():
    response = app.test_client().get('/bookmarks/remove/1', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса добавления закладок не ок"
