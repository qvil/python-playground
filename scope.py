def scope_test():
    def do_local():
        data = "local data"

    def do_non_local():
        nonlocal data
        data = "nonlocal data"

    data = "test data"

    do_local()
    do_non_local()


scope_test()


def scope_test():
    def do_local():
        data = "local data"

    def do_non_local():
        nonlocal data
        data = "nonlocal data"

    data = "test data"

    do_local()
    print(data)
    do_non_local()
    print(data)


scope_test()


def func1():
    def func2():
        data = "local?"
        print(data)

    def func3():
        print(data)

    func2()
    func3()


func1()
