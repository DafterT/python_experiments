from functools import wraps


def repeat(num):
    def repeat_decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            result = [fun(*args, **kwargs) for i in range(num)]
            return result

        return wrapper

    return repeat_decorator


@repeat(5)
def hello_world():
    return 'Hello world!'


def main():
    print(hello_world())


if __name__ == '__main__':
    main()
