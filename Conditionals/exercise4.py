# Refactor ternary expression to an if statement 

def foo():
    return True

def qux():
    pass

def func():
    return ('bar' if foo() else qux())

def func_refactor():
    if foo():
        return 'bar'
    else:
        qux()