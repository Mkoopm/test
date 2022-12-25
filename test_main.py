import main


def test_square():
    square = main.Square

    assert square.is_inside(2, 1) == False
