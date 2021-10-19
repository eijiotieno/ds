def main():
    # dictionary = {
    #     "name": 'Eiji Otieno',
    #     "age": 23,
    # }

    # print(dictionary["name"])
    # def step(a, b):
    #     return a, a + b

    # a, b = 0, 1

    # for i in range(n):
    #     a, b = step(a, b)
    #     print(a, b)
    # return a

    # class Person(object):

    #     species = "Homo Sapiens"

    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age

    #     def __str__(self):

    #         return self.name

    #     def rename(self, renamed):
    #         self.name = renamed

    #         print("name is {}".format(self.name))

    # class D(object):
    #     multiplier = 2

    #     @classmethod
    #     def f(cls, x):
    #         print(cls.multiplier * x)
    #         return cls.multiplier * x

    #     @staticmethod
    #     def g(name):
    #         print("hello, %s" % name)

    # D.f(12)
    # D.g("eiji")

    # class Rectangle:
    #     def __init__(self, w, h):
    #         self.w = w
    #         self.h = h

    #     def area(self):
    #         print(self.w * self.h)
    #         return self.w * self.h

    #     def perimeter(self):
    #         return 2 * (self.w + self.h)

    # Rectangle.area(23)
    # class Person(object):
    #     def __init__(self, first_name, last_name, age):
    #         self.first_name = first_name
    #         self.last_name = last_name
    #         self.age = age
    #         self.full_name = first_name + "" + last_name

    #     def greet(self):
    #         print("hello, my name is" + self.full_name + ".")

    # Person.greet()

    # class Files:
    #     with open("file.txt", "w") as f:
    #         f.write("hello world")
    #         # for i in range(5):
    #         #     f.write("hello wolrd\n")

    # Files

    class ReadFile:
        with open("file.txt", "r") as rf:
            lines = rf.read()
            print(lines)

            # for i in range(len(lines)):
            #     print("line " + str(i) + ": " + lines)
            # while True:
            #     cur_line = rf.readline()

            #     if cur_line == "":
            #         break

            #     print(cur_line)
            # for i in rf:
            #     print(i)
            # rf.readline()

    ReadFile


if __name__ == "__main__":
    main()
