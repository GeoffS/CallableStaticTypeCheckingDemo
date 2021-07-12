from abc import ABC, abstractmethod
from typing import Callable


class Foo(ABC):
    @abstractmethod
    def param(self) -> str:
        pass


class FooImpl(Foo):
    def __init__(self, foo_param: str):
        self._param = foo_param

    def param(self) -> str:
        return self._param


def foo_client(factory: Callable[[str], Foo]) -> str:
    foo = factory("foo_client value-added parameter")
    return f'foo.param() = {foo.param()}'


def foo_factory_correct_signature(foo_param: str) -> Foo:
    return FooImpl(foo_param)


def foo_factory_wrong_signature() -> Foo:
    return FooImpl("gotta have something...")


if __name__ == "__main__":
    res1 = foo_client(lambda foo_param: FooImpl(foo_param))
    res2 = foo_client(foo_factory_correct_signature)

    # Static type checking errors not caught by pycharm
    # These are caught by mypy.
    res3 = foo_client(lambda: FooImpl("foo_param"))
    res4 = foo_client(foo_factory_wrong_signature)

    print('Done!')
