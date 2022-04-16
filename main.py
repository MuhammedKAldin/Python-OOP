# class Car:
#     def __init__(self,brand,model,color,wheels):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.wheels = wheels


# cheverollet = Car("Chevrollete","Tahoe","red",5)
# print(cheverollet.model)

#====================================
# Class Inhertiance
# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def eyeSight(self):
#         print("I Can See")


# class Cat(Animal):
#     def purr(self):
#         print("Meooow !")
        
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#         super().eyeSight() # => getting the Super class methods 
        
# germanShephard = Dog("Sam")
# #germanShephard.eyeSight() # =>Already called inside bark() by the super() method 
# germanShephard.bark()
#
#===============================================================

#Queue Implementation
# class Queue:
#     def __init__(self, contents):
#         self._hiddenlist = list(contents)

#     def push(self, value):
#         self._hiddenlist.insert(0, value)

#     def pop(self):
#         return self._hiddenlist.pop(-1)

#     def __repr__(self):
#         return "Queue({})".format(self._hiddenlist)

# queue = Queue([1, 2, 3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue._hiddenlist)

#===============================================================
# Class Static Methods 
# Doing a Method inside class with another parameter than the init
# @classmthod

# A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
# CLASS METHODS => marked with a classmethod decorator. (@classmethod) 
# # 
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     @classmethod
#     def new_square(cls, side_length):
#         return cls(side_length, side_length)

# square = Rectangle.new_square(5)
# print(square.calculate_area()) 
#=======================================
#=======================================

# Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator.
# STATIC METHODS => MARKED WITH (@staticmethod && FONT USE cls no self as the first parameter or)
# Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.

#========================================================================
# Class Attributes => Read Only => cant be modified
    # @property
    # def pineapple_allowed(self):
    #     return False 
    
#Introducing Setter/Getter into here to read/write the values of Attrubutes which are read only by default
# PROPETY SETTER => @PROPERTY.SETTER
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False

#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed

#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "Sw0rdf1sh!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Alert! Intruder!")

# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)

#++++++++++++++++++++++++++++++++++++++++++
# General Implmenetation of previous examples
# class Goblin(GameObject):
#   def __init__(self, name):
#     self.class_name = "goblin"
#     self.health = 3
#     self._desc = " A foul creature"
#     super().__init__(name)

#   @property
#   def desc(self):
#     if self.health >=3:
#       return self._desc
#     elif self.health == 2:
#       health_line = "It has a wound on its knee."
#     elif self.health == 1:
#       health_line = "Its left arm has been cut off!"
#     elif self.health <= 0:
#       health_line = "It is dead."
#     return self._desc + "\n" + health_line

#   @desc.setter
#   def desc(self, value):
#     self._desc = value

# def hit(noun):
#   if noun in GameObject.objects:
#     thing = GameObject.objects[noun]
#     if type(thing) == Goblin:
#       thing.health = thing.health - 1
#       if thing.health <= 0:
#         msg = "You killed the goblin!"
#       else: 
#         msg = "You hit the {}".format(thing.class_name)
#   else:
#     msg ="There is no {} here.".format(noun) 
#   return msg
#++++++++++++++++++++++++++++++++++++++++++
# You could create different classes (e.g., elves, orcs, humans), 
# fight them, make them fight each other, and so on.
#------------------------------------------
# Juice Maker
# class Juice:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity

#     def __str__(self):
#         return (self.name + ' ('+str(self.capacity)+'L)')

#     def __add__(self,c):
#         return self.name+'&'+c.name+" ({}L)".format(self.capacity+c.capacity)


# a = Juice('Orange', 1.5)
# b = Juice('Apple', 2.0)

# result = a + b
# print(result)

#========================================================================
