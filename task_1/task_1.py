def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, arg in enumerate(args):
            if not isinstance(arg, list(annotations.values())[i]):
                raise TypeError

        for name, arg in kwargs.items():
            if not isinstance(arg, annotations[name]):
                raise TypeError

        return func(*args, **kwargs)

    return wrapper
