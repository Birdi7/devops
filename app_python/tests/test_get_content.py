from ..app import get_content


def test_get_content():
    assert "moscow" in get_content()
