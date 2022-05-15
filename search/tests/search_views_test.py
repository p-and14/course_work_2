from main import app


def test_search_status():
    response = app.test_client().get('/search/', follow_redirects=True)
    assert response.status_code == 200, "Статус-код запроса кандидатов не ок"
