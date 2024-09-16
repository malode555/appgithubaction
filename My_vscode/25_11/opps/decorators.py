

def decor(func):
    def inner(name):
        if name == 'asd':
            print('Hello asd bad morning')
        else:
            func(name)
    return inner
@decor
def wish(name):
    print('Hello',name,'Good morning')
#wish('asd')

wish('mayur')

wish('mahesh')