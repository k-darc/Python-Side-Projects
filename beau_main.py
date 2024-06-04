# name = 'Beau is cool'
# print(name[-1]) -1 starts at the last character
# print(name[1:7]) This is slicing, it'll return index 1 through 3
# print(name[:5]) Blank space at the start will get everything before index 5, same for a blank AFTER the colon


# done = False # You can put a zero, False or a blank quote "" & it'll always be false. Any other number will be true, even a negative.
# if done:
#     print("yes")
# else:
#     print("no")


# Round will round to the highest number
# print(round(5.49, 1))


# This is better than...
# age = int(input("What's your age? "))
# print(f"Your age is {age}")
# This...
# age = input("What is your age? ")
# print("Your age is " + age)


        # TUPLES - create immutable groups of objects (once created, they can't be modified) #############
# names = ("Roger", "Syd")

# names[-1]
# names.index("Roger")
# len(names)
# print("Roger" in names)
# print(sorted(names))
# newTuple = names + ("Tina", "Quincy")


        # DICTIONARIES #############
# dog = {"name": "Roger", "age": 8, "color": "green"}
# dog["favorite food"] = "Meat"
# del dog["color"]
# dogCopy = dog.copy()
# print(dog)


        # SETS #############
# set1 = {"Roger", "Syd"}
# set2 = {"Luna"}

# mod = set1 | set2
# print(mod)


        # FUNCTIONS #############
# def hello(name):
#     print("Hello " + name + "!")
#     return name, "Beau", 8

# print(hello("Syd"))


        # OBJECTS - ALMOST EVERYTHING IN PYTHON IS AN OBJECT #############
# age = 8
# print(age.real)
# print(age.imag)
# print(age.bit_length())


# items= [1, 2]
# items.append(3)
# items.pop()
# print(id(items))


        # LOOPS #############
# count = 0
# while count < 10:
#     print("The condition is True")
#     count += 1
# else:
#     print("After the loop")


        # FOR LOOPS #############
# items = ["beau", "Syd", "quincy"]
# for item in items:
#     if item == 2:
#         continue
#     print(item)


        # CLASSES #############
# class Animal:
#     def walk(self):
#         print("Walking...")

# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print("woof!")

# roger = Dog("Roger", 8)

# print(roger.name)
# print(roger.age)
# roger.bark()
# roger.walk()


        # EXCEPTIONS #############
# try:
#     raise Exception("An error is here!")
# except Exception as error:
#     print(error)


# class DogNotFoundException(Exception):
#     print("inside")
#     pass
# try:
#     raise DogNotFoundException()
# except DogNotFoundException:
#     print("Dog not found!")


        # Operator Overloading #############
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd)