from plover_vcs.vcs.vcs_exception import VcsException
import inspect


def wrap_exceptions():
    """
    Decorator that wraps all methods of a class with
    the exception_decorator
    :return: decorator function
    """
    def decorate(cls):
        for name, fn in inspect.getmembers(cls, inspect.isfunction):
            setattr(cls, name, exception_decorator(fn))
        return cls
    return decorate


def exception_decorator(func):
    """
    Decorator that catches all exceptions and wraps them
    in the generic VcsException
    :param func: function to wrap
    :return: decorator function
    """
    def decorated(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise VcsException(e)
    return decorated
