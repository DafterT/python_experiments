from _1_upper_case import upper_case_decorator
from _2_logger import logger_decorator


@upper_case_decorator
@logger_decorator
def hello_world_1():
    return 'Hello world!'


@logger_decorator
@upper_case_decorator
def hello_world_2():
    return 'Hello world!'


def main():
    hello_world_1()
    """
    Function name: hello_world_1
    Input arguments:
        Not positional: ()
        Positional: {}
    Result: Hello world!
    """
    hello_world_2()
    """
    Function name: hello_world_2
    Input arguments:
        Not positional: ()
        Positional: {}
    Result: HELLO WORLD!
    """


if __name__ == '__main__':
    main()
