#####any function
#it is true if any one is true and false when all are false
# print(any(num%2==0 for num in [2,4,6,8]))
# print(any(num%2==0 for num in [2,4,5,6,8]))

# #####all function
# #it is true if all are true and false if even single is false
# print(any(num%2==0 for num in [2,4,6,8]))
# print(any(num%2==0 for num in [2,4,5,6,8]))

def fun(*args):
    print(all(type(num)==int or type(num)==float for num in args))
fun(1,2,3,'a')

print(all(type(num)==int or type(num)==float for num in (1,2,3,'a')))

print(any(list(num%2==0 for num in list(range(1,11)))))


