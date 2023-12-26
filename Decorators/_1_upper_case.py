from functools import wraps


def upper_case_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@upper_case_decorator
def hello_world():
    return 'Hello world!'


def main():
    print(hello_world())
    print(hello_world.__name__)


if __name__ == '__main__':
    main()
