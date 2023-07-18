from typing import Any, Callable, Dict

from loguru import logger


def processing_wrapper(
    idx: int,
    total: int,
    payload: Dict[str, Any],
    func: Callable,
    echo_step: int = 0,
) -> Any:
    # Auto decide echo_step
    if echo_step == 0:
        echo_step = round(total / 5)
    if idx % echo_step == 0:
        logger.info(f"#{idx}/{total}, payload: {payload}")
    res = func(**payload)
    return res
