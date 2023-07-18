from yiutils.processing import processing_wrapper


def example_func(x: int) -> int:
    res = x + 1
    return res


def test_processing_wrapper():
    series = list(range(10))
    processing_res = [
        processing_wrapper(
            idx=idx, total=len(series), payload={"x": _}, func=example_func
        )
        for idx, _ in enumerate(series)
    ]
    assert len(processing_res) == len(series)
