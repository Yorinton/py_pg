def example_func(param1, param2):
    """Example fuction with types documented in the docstring

    Args:
        param1 (int): The first param
        param2 (int): The second param

    Returns:
        bool: The return value, True for success

    """
    print(param1)
    print(param2)
    return True

# python docsを表示
print(example_func.__doc__)
help(example_func)