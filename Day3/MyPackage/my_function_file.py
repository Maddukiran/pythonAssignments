

def Stack_calls(start_fun, log_fun, lst1, lst2):
    def wrapper(func):
        def Caller(*arg):
            start_fun(*lst1)
            func(*arg)
            log_fun(*lst2)
        return Caller
    return wrapper