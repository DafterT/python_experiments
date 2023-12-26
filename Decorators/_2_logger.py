from functools import wraps


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function name: {func.__name__}')
        print(f'Input arguments:\n'
              f'\tNot positional: {args}\n'
              f'\tPositional: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result

    return wrapper


@logger_decorator
def hello_world():
    return 'Hello world!'


def main():
    print(hello_world())
    print(hello_world.__name__)


if __name__ == '__main__':
    main()
