#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xray.py

Source code : https://github.com/yang445786754/call_function_with_timeout

Author :

* Tony_9410 - tony_9410@foxmail.com


"""

from thread_with_results import ThreadWithResult, stop_thread
from typing import Any, Callable


def _call_with_timeout(func=None, __timeout=None, *args, **kwds):
    task = ThreadWithResult(
        func,
        *args,
        **kwds
    )
    task.start()
    task.join(timeout=__timeout)
    stop_thread(task)
    return task.done, task.timeout, task.error, task.results


class SetTimeout(object):
    """ __call__()
        @return (task.done, task.timeout, task.error, task.results)
        @return (是否执行完成, 是否超时, 是否异常, 任务执行结果)
    """
    def __init__(self, func, timeout=None) -> None:
        self.func = func
        assert isinstance(func, Callable), '您需要传一个可以执行的方法'
        self.timeout = timeout

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return _call_with_timeout(
            self.func, self.timeout, *args, **kwds)


class SetTimeoutDecorator(object):
    """ 
        @return (task.done, task.timeout, task.error, task.results)
        @return (是否执行完成, 是否超时, 是否异常, 任务执行结果)
    """
    def __init__(self, timeout=None) -> None:
        self.timeout = timeout

    def __call__(self, func) -> Any:
        self.func = func
        assert isinstance(func, Callable), '您需要装饰一个可以执行的方法'
        def wrapper( *args: Any, **kwds: Any):
            return _call_with_timeout(
                self.func, self.timeout, *args, **kwds)
        return wrapper
