# # this funcking takes variable number of args
# def fn(*args):
#     return args
#
#
# array = [1, 2, 3]
# # here * operation is just unpacking the array into individual elements
# print("The result of this thinge is : ", fn(*array))
#
# def function(**args):
#     return args
#
# obj = {'a': 1, 'b': 2, 'c': 3}
#
#
# # here ** operation is just unpacking the object into individual key-value pairs
# print("The result of this thinge is : ", function(**obj))
# print("Tne result of this thinge is : ", function(a=1, b=2, c=3))
#

# scope
#
# x = 10
#
# print("The initial content of x is : ", x)
#
#
# def set_x(number):
#     x = number
#     print("The content of the x is : ", x)
#
#
# set_x(4)
#
#
# print("The content of the x after calling set_x function is : ", x)
#
#
# def set_global_x(number):
#     global x
#     x = number
#     print("The content of the x is : ", x)
#
#
# set_global_x(43)
#
# print("The content of the x after calling set_global_x function is : ", x)

# some first class function

# def function(x):
#     def fn(y):
#         return x + y
#     return fn
#
#
# # here this variable add_10 contain the function fn so it will take another value then the function will return the sum of the preceeding value
# # that is there and add the content 
# add_10 = function(10)
# print("Tne content of add_10 is ", add_10(20))


# anonymous functin they say 

# print(" is x greater then 10 : ", (lambda x: x > 10)(32))
#
# a = 4
# b = 4
# print("The sum of a and b is ", (lambda x, y: x + y)(a, b))


# # some poop
# class Programmar:
#     species = "H. sapiens"
#
#     # this is like default constructor 
#     def __init__(self, msg, name):
#         self.name = name
#         self.msg = msg
#
#     def say_my_name(self):
#         print("The name", self.name)
#
#     def say_buzz_word(self, buzz_word):
#         print(self.name, ", my buzz word is ", buzz_word)
#
#
#     #`@classmethod` marks a method that receives the class (`cls`) instead of an instance (`self`).
#     # Here `get_species` accesses the class attribute `species`, so calling `MyClass.get_species()` (or via an instance) returns whatever `species` is defined on that class.
#
#     @classmethod
#     def get_species(cls):
#         return cls.species
#
# # `self.species` works only if you have an instance and species isn’t overridden on the instance.
# #`cls.species` ensures you read the class attribute itself, 
# # so the method can be called either on the class or any instance and still refer to the shared class-level value.
# # `@classmethod` makes `cls` the first parameter, giving direct access to the class object itself.
# # Using `cls.species` ensures the method always reads the shared class-level attribute, even if someone overrides `species` on an individual instance or calls the method without creating an instance.
# # This keeps the method’s behavior strictly tied to class state.
#
#     @staticmethod
#     def what():
#         return " I am a programmar and I am called without instance or class reference"
#
# # `@staticmethod` defines a method that doesn’t need `self` or `cls`; it’s just a plain function namespaced inside the class.
# # You can call `Programmar.what()` without creating an instance, and it can’t access instance or class data unless you pass it in.
#
#     @property 
#     def info(self):
#         return f"{self.name} says {self.msg}"
#     # Using `@property` makes `info` accessible like an attribute (e.g., `obj.info`) while allowing it to compute its value dynamically.
#     # This is useful for creating read-only attributes or computed properties without needing to call a method explicitly
#
# # this is the setter for the property info
#     @info.setter
#     def info(self, value):
#         name, msg = value.split(" says ")
#         self.name = name
#         self.msg = msg
#
# # this is the deleter for the property info
# # after deleting the info property both name and msg will be deleted from the object
# # so accessing info property after deleting it will raise an attribute error
#     @info.deleter
#     def info(self):
#         del self.name
#         del self.msg
#
#
#
# # this is the main entry point of the program
# # if the file is run directly then this block will be executed
#
# # When a Python interpreter reads a source file it executes all its code.
# # This __name__ check makes sure this code block is only executed when this
# # module is the main program.
# if __name__ == "__main__":
# # creating an instance of the Programmar class
# # passing the msg and name as arguments
#         programmar = Programmar("Hello World", "Alice")
#         print(programmar.info)  # Accessing the property
#         programmar.info = "Bob says Hi there!"  # Using the setter
#         print(programmar.info)  # Accessing the updated property
#         del programmar.info  # Using the deleter
# # print(programmar.info)  # This will raise an AttributeError since name and msg are
# # deleted from the object
#         print("The species of programmar is : ", Programmar.get_species())
#         print(Programmar.what())
#
#
#
#
# # MRO (Method Resolution Order) - __mro__ Explained
#
# # What is __mro__?
# # It's the "search path" Python follows when looking for methods in classes
# # Think of it like checking your pocket, then bag, then car for your keys
#
# # ============================================
# # Example 1: Simple Inheritance
# # ============================================
#
# class Animal:
#     def speak(self):
#         return "Some sound"
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Puppy(Dog):
#     pass  # Puppy doesn't define speak()
#
# # Check the MRO
# print("Puppy MRO:", Puppy.__mro__)
# # Output: (<class 'Puppy'>, <class 'Dog'>, <class 'Animal'>, <class 'object'>)
#
# my_puppy = Puppy()
# print(my_puppy.speak())  # Prints "Woof!" (found in Dog class)
#
# print("\n" + "="*50 + "\n")
#
# # ============================================
# # Example 2: Multiple Inheritance
# # ============================================
#
# class A:
#     def method(self):
#         return "A"
#
# class B(A):
#     def method(self):
#         return "B"
#
# class C(A):
#     def method(self):
#         return "C"
#
# class D(B, C):
#     pass
#
# # Check the MRO - this is where it gets interesting!
# print("D MRO:", D.__mro__)
# # Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
#
# print(D().method())  # Prints "B" because B comes before C in the MRO
#
# print("\n" + "="*50 + "\n")
#
# # ============================================
# # Example 3: Superhero (Classic Example)
# # ============================================
#
# class Human:
#     def __init__(self, name):
#         self.name = name
#     
#     def speak(self):
#         return f"{self.name} says hello"
#
# class Hero(Human):
#     def __init__(self, name, power):
#         super().__init__(name)
#         self.power = power
#     
#     def use_power(self):
#         return f"{self.name} uses {self.power}!"
#
# class Superhero(Hero):
#     def __init__(self, name, power, costume):
#         super().__init__(name, power)
#         self.costume = costume
#
# # Check the MRO
# print("Superhero MRO:", Superhero.__mro__)
# # Output: (<class 'Superhero'>, <class 'Hero'>, <class 'Human'>, <class 'object'>)
#
# superman = Superhero("Clark", "flight", "blue suit")
# print(superman.speak())  # Found in Human class
# print(superman.use_power())  # Found in Hero class
#
# # Key Takeaway: Python searches left-to-right, bottom-to-top
# # Always checks the current class first, then parent classes in order

# Generators in Python
# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# Generators are defined using functions and the yield statement.
# this basically doubles the even numbers from the iterable
# also this makes use of yield keyword to yield the values one by one
# which makes it memory efficient as it doesn't store all the values in memory at once
# it yields the values one by one as they are requested
# so it is more memory efficient for large datasets
# hence generators are often used for processing large datasets or streams of data where memory efficiency is important.

# def double_even(iterable):
#     for value in iterable:
#         if value % 2 == 0:
#             yield value * 2
#
#
# if __name__ == "__main__":
#     nums = [1, 2, 3, 4, 5, 6]
#     for doubled in double_even(nums):
#         print(doubled)
