#old school:--
# def fun(a,b):
#     return a+b;


# lambda is not a function but it can be used for evaluation
# it is a type of anonymous function
# add = lambda a,b : a+b
# print(add(10,20))
# print(add)
# print(type(add))



####old school:--
# def fun(s):
#     return len(s) > 5
# print(fun('abcd'))
# print(fun('abcdef'))

##using lambda expression with comprehension:----
# res = lambda s :True if len(s) > 5 else False
##shortenung lambde:--
# res = lambda s : len(s) > 5
# print(res('abcd'))
# print(res('abcdef'))