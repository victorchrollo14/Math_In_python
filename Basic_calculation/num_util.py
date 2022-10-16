import numpy as np
import sympy as smp


x = smp.symbols('x')
def finding_roots(expr):
    for i in range(11):
        func_of_x = expr.subs(x, i)
        func_of_x1 = expr.subs(x, i+1)

        if((func_of_x > 0 and func_of_x1 < 0) or (func_of_x < 0 and func_of_x1 > 0)):
            return i, i+1

def falsi_formula(expr, m, n):
    a, b = m, n
    fa = expr.subs(x, a)
    fb = expr.subs(x, b)
    print(f"{fa}\n{fb}")

    formula = (a * fb) + (b * fa)/fb - fa
    return float(formula)

def temp_roots(expr, m, n):
    sub_vals = np.arange(m, n, 0.1)
    for i in sub_vals:
       f1 = expr.subs(x, i)
       f2 = expr.subs(x, i + 0.1)

       if((f1 > 0 and f2 < 0) or (f1 < 0 and f2 > 0)):
          return i, i + 0.1
       