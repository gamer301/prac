import abc
from abc import ABC, abstractmethod
# @staticmethod  , does not receive self when called , bound to class , can't modify class variable and methods , oblivious to class var,methods
# nested class help with encapsulation
class parent(ABC):
    @abstractmethod
    def geeks(self):
        return "parent class"
    
class MyClass:
    @classmethod
    def class_method(cls):
        print("Class Method")    

class MyClass:
    def instance_method(self):
        print("Instance Method")    
#g=parent() 
#g.geeks()   will give error since you can't call an abstract class , hides info 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        super().method() # you don't need the parent class name if you use super
        print("Child method")

obj = Child()
obj.method()



class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):  # MRO for multiple inheritance left to right 
    pass

obj = D()
obj.method()

#Output: B method

m = [1,2,3]
n=m.copy()
print(m,n)
n.append(4)
print (m,n)
x=range(10)
print(x)

str="hello"
l= [str,"no","aa"]
print(sorted(l))
print ("-".join(sorted(l)))

# Print names of people over 18
ages = {"Alice": 20, "Bob": 17, "Charlie": 25}
u=ages.items()
print(u)

for x,y in u :
    if y>18 :
        print (f"{x}:{y}")

input_string = "Hello, World!"
x=list(input_string)
x.sort(reverse=True)
print(x)
vowel_count = sum(1 for char in input_string if char.lower() in 'aeiou')


list_of_tuples = [(k, v) for k, v in states_tz_dict.items()]
print(list_of_tuples)


user_input = input("Enter a string: ")
reverse_string = list(user_input)
reverse_string.sort(reverse=True)
#rev_sort=sorted(reverse_sort,reverse=True)
#rev_order=sorted(reverse_sort)
# input_string[::-1]
#len()
#check is not / in "sample"  
#Check if "free" is present in the following text:
#list/string/dict .count()
#len() for string

txt = "The best things in life are free!"
print("free" in txt)

print ("".join(reverse_string))

#string[sta]

#x_merge = list1 | list2
#x_common= list1 & list2

my_list = [1, 2, 3]
try:
    result = my_list.nonexistent_method()
    raise AttributeError("custom")
except AttributeError as e: # if no e it will just act to bypass error 
    print(f"AttributeError: {e}") # e='list' object has no attribute 'nonexistent_method' ## <-- defualt error discription 