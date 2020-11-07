# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self._price=max(price,0)
#         # self.complete_specification = f"{self.brand} : {self.model} : {self.price}"

#     @property    # any function with property decorator can be called as a property(without using paranthesis)
#     def complete_specification(self):
#         return f"{self.brand} : {self.model} : {self._price}"
    
#     @property
#     def show_price(self):
#         # return self._price
#         pass
#     @show_price.setter
#     def xyz(self,new_price):
#         self._price=max(new_price,0)
    
#     # @property
#     # def make_a_call(self):
#     #     return f"calling : {self.number}"
#     # @make_a_call.setter
#     # def newxyz(self,new_number):
#     #     self.number=max(new_number,0)
#             ###or##
#     def newxyz(self,new_number):
#         self.number=max(new_number,0)
    
# phone1=Phone('apple','iphone-x',70000)
# print(phone1.complete_specification)
# phone1.xyz=-50000
# print(phone1.show_price)
# print(phone1.complete_specification)
# # phone1.newxyz=-111
# # print(phone1.make_a_call)
#             ###or##
# phone1.newxyz(-111)
# print(phone1.__dict__)

# # price class variable value can be changed at any time so it can be made negative so to prevent that
# # we make setter function with any name and pass a new value to it for evaluation
# # as we made a setter function so it need a getter function too so we make a getter function with
# # property decorator----it can be empty or we can give any working to it



# def foo(m):
#     if m == 0:
#       return(0)
#     else:
#       return(m+foo(m-1))