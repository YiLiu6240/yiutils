import pytest

from yiutils.failsafe import failsafe


@failsafe
def good():
    return 1


@failsafe
def bad(x: int = 0):
    y = 12 / 0  # noqa
    return x


@failsafe(silent=True)
def silent_bad(x: int = 0):
    y = 12 / 0  # noqa
    return x


def test_good():
    res = good()
    assert isinstance(res, tuple)
    assert len(res) == 3
    assert res == (1, True, None)


def test_bad():
    with pytest.warns(match="division by zero") as record:
        res = bad()
    assert isinstance(res, tuple)
    assert len(res) == 3
    assert res[0] is None
    assert isinstance(res[1], ZeroDivisionError)
    assert res[2] == {"x": 0}
    assert len(record) == 1


def test_silent_bad():
    res = silent_bad()
    assert isinstance(res, tuple)
    assert len(res) == 3
    assert res[0] is None
    assert isinstance(res[1], ZeroDivisionError)
    assert res[2] == {"x": 0}
