import functools
import warnings
from inspect import getcallargs
from typing import Any, Callable, Optional, Tuple, Union

_CONTINGENT_ERROR = Union[bool, Exception]
_CONTEXT = Optional[Any]
_FAILSAFE_RES = Tuple[Optional[Any], _CONTINGENT_ERROR, _CONTEXT]
_MESSAGE_TEMPLATE = "failsafe: error: {error}; context: {context}"


def failsafe(
    f_py: Optional[Callable[..., Any]] = None, silent: bool = False
) -> Callable[..., Any]:
    """Decorator that wraps functions to catch and handle exceptions gracefully.

    Returns a tuple of (result, error_flag, context) instead of raising
    exceptions. If an exception occurs, the function returns None as the
    result, the exception as the error_flag, and the function arguments
    as context.

    Source:

    - https://stackoverflow.com/a/60832711
    - https://stackoverflow.com/a/69030553

    Args:
        f_py: The function to wrap (when used without parentheses)
        silent: If True, suppresses warning messages when exceptions occur

    Returns:
        Decorated function that returns (result, error_flag, context) tuple
        where:
        - result: Function return value or None if exception occurred
        - error_flag: True if successful, Exception object if failed
        - context: None if successful, function arguments dict if failed

    Examples:
        @failsafe
        def divide(a, b):
            return a / b

        result, error, context = divide(10, 2)  # (5.0, True, None)
        result, error, context = divide(10, 0)  # (None, ZeroDivisionError(...), {'a': 10, 'b': 0})
    """

    def _failsafe(func: Callable[..., Any]) -> Callable[..., _FAILSAFE_RES]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> _FAILSAFE_RES:
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
                        error=f"{type(error).__name__} -- {error}",
                        context=context,
                    )
                    warnings.warn(message, stacklevel=2)
            wrapper_res: _FAILSAFE_RES = (func_res, contingent_error, context)
            return wrapper_res

        return wrapper

    if callable(f_py):
        return _failsafe(f_py)  # type: ignore[return-value]
    else:
        return _failsafe  # type: ignore[return-value]
