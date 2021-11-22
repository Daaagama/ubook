"""
Tests for lab6, lab7
"""


def test_lab6_feedback_form(client):
    """
    Template validation
    """
    rv = client.get('/labs/lab6', follow_redirects=True)
    assert rv.status_code == 200
    assert "email" in rv.data.decode("utf-8")
    assert "message" in rv.data.decode("utf-8")
    assert "submit" in rv.data.decode("utf-8")


def test_lab6_form_handler(client):
    """
    Test the feedback form handler
    """
    # Test for normal values
    rv = client.post("/labs/lab6/", data={
        "email": "myemail@example.com",
        "message": "test message"
    })
    assert rv.status_code == 200
    assert "myemail@example.com" in rv.data.decode("utf-8")
    assert "test message" in rv.data.decode("utf-8")

    # Test for empty email
    rv = client.post("labs/lab6/", data={
        "message": "my message"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "та" in rv.data.decode("utf-8")  # Check for flash message

    # Test for empty message
    rv = client.post("labs/lab6/", data={
        "email": "test@example.com"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "та" in rv.data.decode("utf-8")  # Check for flash message

    # Test for html inside message
    rv = client.post("/labs/lab6/", data={
        "email": "myemail@example.com",
        "message": "Some <h1>HTML</h1>"
    })
    assert "Some &lt;h1&gt;HTML&lt;/h1&gt;" in rv.data.decode("utf-8")
