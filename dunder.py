# __str__  ==>  it is used by dev. to return string and used in strings basically
# __repr__ ==>  it is used by dev. to return object while it can return string too
class A:
    def __init__(self,a,b,name):
        self.a=a
        self.b=b
        self.name=name

    def __str__(self):
        return f'__str__ : {self.a} : {self.b}'

    def __repr__(self):
        return f'__repr__ : {self.a} : {self.b}'

    def __len__(self):
        return len(self.name)

obj = A(1,2,'aabhinaav')
# just calling, and interpreter will decide what to call:-
print(obj)
# calling as function:-
print(str(obj))
print(repr(obj))
# calling as method:-
print(obj.__str__())
print(obj.__repr__())
# calling __len__ :-
print(len(obj))
print(obj.__len__())
# print(objestname) ==> only __repr__ is present then it will be called
#                       only __str__ is present then it will be called
#                       both present then str will be called