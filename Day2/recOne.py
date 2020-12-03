def func(num):
    if(num<=10):
        print(num, end=' ')
        func(num+1)
func(1)