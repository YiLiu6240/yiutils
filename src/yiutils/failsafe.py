from typing import Callable, Optional, Any, Union

import functools

_CONTINGENT_ERROR = Union[bool, Exception]
_FAILSAFE_RES = Tuple[Optional[Any], _CONTINGENT_ERROR]

def failsafe(f_py: Optional[Callable] = None, silent: bool = False) -> _FAILSAFE_RES:
    # https://stackoverflow.com/a/60832711
    def _failsafe(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> _FAILSAFE_RES:
            wrapper_res: _FAILSAFE_RES
            error: _CONTINGENT_ERROR
            try:
                func_res = func(*args, **kwargs)
                contingent_error = True
            except Exception as error:
                func_res = None
                contingent_error = error
            wrapper_res = (func_res, error)
            return wrapper_res
        return wrapper
    failsafe_res = _failsafe(f_py) if callable(f_py) else _failsafe
    return failsafe_res
