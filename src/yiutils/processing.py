from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional

import simple_parsing
from loguru import logger
from simple_parsing import field


def processing_wrapper(
    idx: int,
    total: int,
    payload: Dict[str, Any],
    func: Callable,
    echo_step: int = 0,
    prefix: str = "",
) -> Any:
    if len(prefix) != 0:
        prefix = prefix + "\t"
    # Auto decide echo_step
    if echo_step == 0:
        echo_step = round(total / 5)
    if idx % echo_step == 0:
        logger.info(f"{prefix}#{idx}/{total}, payload: {payload}")
    res = func(**payload)
    return res


@dataclass
class BaseArgs:
    dry_run: bool = field(alias="dry-run", action="store_true")
    trial: bool = field(action="store_true")
    num_samples: Optional[int] = None


def make_base_args() -> BaseArgs:
    base_args: BaseArgs = simple_parsing.parse(BaseArgs)
    return base_args
