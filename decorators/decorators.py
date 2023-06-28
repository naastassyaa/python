"""This module includes decorators for function validation and logging.
Module Contents:
- history: A decorator that logs the name of a function and the current timestamp to a file.
- validate_snake_case: A decorator that validates if
a function name follows the snake case convention."""
import datetime
import logging


def history(func):
    """A decorator that logs the name of the function and the current timestamp
        to a file called 'history.txt' in UTF-8 encoding.
        Args:
            func: The function to be decorated.
        Returns:
            The wrapped function."""

    def wrapper(*args, **kwargs):
        """Wrapper function that logs the function name and timestamp
        before executing the decorated function.
        Args:
            *args: Arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.
        Returns:
            The result of the decorated function."""
        with open("history.txt", "a", encoding="UTF-8") as file:
            file.write(f"Name: {func.__name__} Time: {datetime.datetime.now()}\n")
        return func(*args, **kwargs)

    return wrapper


def validate_snake_case(func):
    """A decorator that validates if the function name follows the snake case convention.
       The function name should be in lowercase and
       consist of only letters, digits, and underscores.
       Args:
        func: The function to be decorated.
       Returns:
        The wrapped function.
       Raises:
        ValueError: If the function name does not
        follow the snake case convention."""

    def wrapper(*args, **kwargs):
        """Wrapper function that validates the function name
            before executing the decorated function.
           Args:
            *args: Arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.
           Returns:
            The result of the decorated function.
           Raises:
            ValueError: If the function name does not follow the snake case convention."""
        function_name = func.__name__
        if not function_name.islower() or not function_name.isidentifier():
            raise ValueError("Function name must be in snake case.")

        return func(*args, **kwargs)

    return wrapper


def logged(exception, mode):
    """A decorator that logs exceptions raised by the decorated function.
        Args:
            exception (Exception): The type of exception to be caught and logged.
            mode (str): The logging mode. Can be either "console" or "file".
        Returns:
            function: The decorated function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as error:
                if mode == "console":
                    logging.basicConfig(format='%(levelname)s - %(message)s')
                    logging.error(str(error))
                elif mode == "file":
                    logging.basicConfig(filename='app.log', filemode='w',
                                        format='%(levelname)s - %(message)s')
                    logging.error(str(error))
            return None
        return wrapper

    return decorator
