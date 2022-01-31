import inspect


def static_class(cls):
    for name, method in inspect.getmembers(cls):
        if (not inspect.ismethod(method) and not inspect.isfunction(method)) or inspect.isbuiltin(method):
            continue
        setattr(cls, name, staticmethod(method))
    return cls
