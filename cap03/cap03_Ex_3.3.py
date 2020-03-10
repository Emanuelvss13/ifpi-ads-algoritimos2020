def linha(g, h):
    print(g, end='')
    print(h) 

def coluna(a, b):
    a(b)
    a(b)
    a(b)

def grade():
    linha(('+ - - - - ' * 3),('+'))
    coluna(print, '|         ' * 4)
    linha(('+ - - - - ' * 3),('+'))
    coluna(print, '|         ' * 4)
    linha(('+ - - - - ' * 3),('+'))
    coluna(print, '|         ' * 4)
    linha(('+ - - - - ' * 3),('+'))
    coluna(print, '|         ' * 4)
    linha(('+ - - - - ' * 3),('+'))
    

grade()