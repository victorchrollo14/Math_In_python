import sympy as smp
from sympy.core import symbols


def with_respect_to():
    wrt_var = input("enter the with respect to variable:(x or y or z)\n")
    return symbols(f"{wrt_var}")


def lower_upper_limit():
    lower_limit = input('enter the lower limit:')
    upper_limit = input('enter the upper limit:')
    return lower_limit, upper_limit
