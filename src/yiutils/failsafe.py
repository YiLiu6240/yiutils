import functools
import warnings
from inspect import getcallargs
from typing import Any, Callable, Optional, Tuple, TypeVar, Union, cast

_CONTINGENT_ERROR = Union[bool, Exception]
_CONTEXT = Optional[Any]
_FAILSAFE_RES = Tuple[Optional[Any], _CONTINGENT_ERROR, _CONTEXT]
_Func = TypeVar("_Func", bound=Callable[..., _FAILSAFE_RES])
_MESSAGE_TEMPLATE = "failsafe: error: {error}; context: {context}"


def failsafe(
    f_py: Optional[Callable] = None, silent: bool = False
) -> Callable[[_Func], _Func]:
    # https://stackoverflow.com/a/60832711
    # https://stackoverflow.com/a/69030553
    def _failsafe(func: _Func) -> _Func:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> _FAILSAFE_RES:
            contingent_error: _CONTINGENT_ERROR
            context: _CONTEXT
            try:
                func_res = func(*args, **kwargs)
                contingent_error = True
                context = None
            except Exception as error:
                func_res = None
                contingent_error = error
                context = getcallargs(func, *args, **kwargs)
                if not silent:
                    message = _MESSAGE_TEMPLATE.format(
                        error="{type} -- {error}".format(
                            type=type(error).__name__, error=error
                        ),
                        context=context,
                    )
                    warnings.warn(message)
            wrapper_res: _FAILSAFE_RES = (func_res, contingent_error, context)
            return wrapper_res

        return cast(_Func, wrapper)

    if callable(f_py):
        failsafe_res = _failsafe(f_py)
    else:
        failsafe_res = _failsafe
    return failsafe_res
