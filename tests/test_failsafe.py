from yiutils.failsafe import failsafe


@failsafe
def good():
    return 1


@failsafe
def bad(x: int = 0):
    y = 12 / 0  # noqa
    return x


def test_good():
    res = good()
    assert isinstance(res, tuple)
    assert len(res) == 3
    assert res == (1, True, None)


def test_bad():
    res = bad()
    assert isinstance(res, tuple)
    assert len(res) == 3
    assert res[0] is None
    assert isinstance(res[1], ZeroDivisionError)
    assert res[2] == {"x": 0}
