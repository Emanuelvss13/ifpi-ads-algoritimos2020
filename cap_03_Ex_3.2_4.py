def do_twice(f):
    f()
    f()

def print_twice():
    print('spam')

do_twice(print_twice)