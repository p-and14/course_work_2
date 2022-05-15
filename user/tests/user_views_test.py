from main import app


def test_user_status():
    response = app.test_client().get('/users/1', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса пользователей не ок"
