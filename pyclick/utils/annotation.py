from __future__ import annotations

from inspect import signature


def get_types_of_function_args(function):
    sig = signature(function)
    args_types = [arg.annotation for arg in sig.parameters.values()]
    # for arg in sig.parameters.values():
    #     print(arg.annotation)
    #     args_types.append(eval(arg.annotation))
    return args_types
