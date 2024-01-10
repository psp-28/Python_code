# class Parent:
#     def __init__(self,name):
#         self.name = name
        
# class Stu(Parent):
#     def __init__(self,name):
#         super().__init__(name)
        
#     def obj(self):
#         #convert list into string 
#         str1 = " "
#         for elements in self.name:
#             str1+= elements
#         print("name is: ")
#         print(" ".join(str1))

# my_str = []

# inp =input("Enter your First Name: ")
# my_str.append(inp)
# inp1 = input("Enter your father's Name: ")
# my_str.append(inp1)
# inp2 = input("Enter your Last Name: ")
# my_str.append(inp2)

# x = Stu(my_str)
# x.obj()


##################################################################################################################

# class Parent:
#     def __init__(self,name):
#         self.name = name
        
# class Stu(Parent):
#     def __init__(self,name):
#         super().__init__(name)
        
#     def obj(self):
#         #convert list into string 
#         str1 = " "
#         for elements in self.name:
#             str1+= elements
#         print("name is: ")
#         print(" ".join(str1))

# my_str = []

# inp = input("Enter your First Name: ")
# my_str.append(inp)
# inp1 = input("Enter your father's Name: ")
# my_str.append(inp1)
# inp2 = input("Enter your Last Name: ")
# my_str.append(inp2)

# x = Stu(my_str)
# x.obj()

##############################################################################################################


class Parent:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name    

class Child(Parent):
    def __init__(self,first_name,mid_name,last_name):
        super().__init__(first_name,last_name)
        self.mid_name=mid_name

first_name = input("Enter your First Name: ")
mid_name = input("\nEnter your Father's Name: ")
last_name = input("\n Enter your Last Name: ")

Child_object = Child(first_name,mid_name,last_name)

#Displaying the results
print(f"\nChild's Full Name: {Child_object.first_name} {Child_object.mid_name} {Child_object.last_name}")
print(f"\nFather's Name: {Child_object.mid_name}")

