# 5
def do_twice(f, g):
    f(g)
    f(g)


def do_four():
    do_twice(print, 'massa')
    do_twice(print, 'massa')

do_four()
