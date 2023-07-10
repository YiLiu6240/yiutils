import functools
import warnings
from typing import Callable, Optional, Any, Union, Tuple
from inspect import getcallargs

_CONTINGENT_ERROR = Union[bool, Exception]
_CONTEXT = Optional[Any]
_FAILSAFE_RES = Tuple[Optional[Any], _CONTINGENT_ERROR, _CONTEXT]

def failsafe(f_py: Optional[Callable] = None, silent: bool = False) -> _FAILSAFE_RES:
    # https://stackoverflow.com/a/60832711
    def _failsafe(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> _FAILSAFE_RES:
            try:
                func_res = func(*args, **kwargs)
                contingent_error = True
                context = None
            except Exception as error:
                func_res = None
                contingent_error = error
                context = getcallargs(func, *args, **kwargs)
                if not silent:
                    message = "failsafe issue detected: error: {error}; context: {context}".format(
                        error="{type} -- {error}".format(type=type(error).__name__, error=error),
                        context=context
                    )
                    warnings.warn(message)
            wrapper_res: _FAILSAFE_RES = (func_res, contingent_error, context)
            return wrapper_res
        return wrapper
    failsafe_res = _failsafe(f_py) if callable(f_py) else _failsafe
    return failsafe_res
