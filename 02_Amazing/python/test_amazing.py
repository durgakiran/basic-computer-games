import pytest
from amazing import build_maze, welcome_header


def test_welcome_header(capsys):
    assert welcome_header() == None
    out, err = capsys.readouterr()
    assert out == (
        "                            AMAZING PROGRAM\n"
        "               CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n\n\n"
    )
    assert err == ""


@pytest.mark.parametrize(
    ("width", "length"),
    [
        (1, 1),
        (1, 0),
        (1, -1),
        (1, 2),
        (2, 1),
    ],
)
def test_build_maze(width, length):
    with pytest.raises(AssertionError):
        build_maze(width, length)
