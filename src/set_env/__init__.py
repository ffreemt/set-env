"""Init."""
from .set_env import set_env


def hello():
    print("Hello from set-env!!")
    return "Hello from set-env!"


__all__ = ("set_env",)
