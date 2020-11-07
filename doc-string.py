# every function in python has string in written in it that defines what it do
print(len.__doc__)


# making user defines doc sting
def fun(a,b):
    '''this function returns the sum of 2 numbers passed'''
    return a+b
print(fun(10,20))
print(fun.__doc__)