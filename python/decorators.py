"""
Subject: Decorators
Date: 2020-10-08
"""


def decorator_function(some_function):
    """Function for returning wrapper function."""
    # Make built in libraries to import here.
    import time

    def wrapper_function(*args, **kwargs):
        """Anything in this code witl be runned together with some_function.

        Arguments: Add *args and **kwargs to allow arbitrtary input to
                   some_function.
        """
        # Start counting
        start = time.time()
        # Run method
        result = some_function(*args, **kwargs)
        # Stop counting
        end = time.time()
        print('Time elapsed: {}'.format(end - start))
        # Retturn input function result
        return result

    return wrapper_function


# Wrappoing decorator
@decorator_function
def say_hello():
    print('Hi Magnus')


# Wrappoing decorator
@decorator_function
def say_hello_with_args(name):
    print('Hi {}'.format(name))


# Execute functions
say_hello()
say_hello_with_args('Magnus Friberg')
