def timefun(func):
    print("xixixi")
    def wrappedfunc(a, b):
        print("hshsh")
        print("%s called at %s"%(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrappedfunc

@timefun
def foo(a, b):
    print(a+b)
