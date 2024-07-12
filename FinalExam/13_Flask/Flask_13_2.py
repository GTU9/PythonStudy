import time


def delay_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_function
def say_hello():
    print('hello')
