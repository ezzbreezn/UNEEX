def ADD(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) + g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) + g
    elif not callable(f) and callable(g):
        return lambda x: f + g(x)
    elif not callable(f) and not callable(g):
        return lambda x: f + g

def SUB(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) - g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) - g
    elif not callable(f) and callable(g):
        return lambda x: f - g(x)
    elif not callable(f) and not callable(g):
        return lambda x: f - g

def MUL(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) * g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) * g
    elif not callable(f) and callable(g):
        return lambda x: f * g(x)
    elif not callable(f) and not callable(g):
        return lambda x: f * g

def DIV(f, g):
    if callable(f) and callable(g):
        return lambda x: f(x) / g(x)
    elif callable(f) and not callable(g):
        return lambda x: f(x) / g
    elif not callable(f) and callable(g):
        return lambda x: f / g(x)
    elif not callable(f) and not callable(g):
        return lambda x: f / g
