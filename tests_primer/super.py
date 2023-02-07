# super() is a special function in Python that allows you to refer to the parent
# class. It is used to call a method on the parent class from the subclass. The
# self object refers to the instance of the subclass and can be processed by a
# method in the parent class, but it must be passed as an argument to the parent
# class's method. The parent class's method can then return the modified self
# object, which can then be passed to methods on the subclass. Here's an example:

class ParentClass:
    def process(self):
        self.value *= 2
        return self

class ChildClass(ParentClass):
    def modify(self):
        self = super().process()
        self.value += 1
        return self

obj = ChildClass()
obj.value = 10
obj = obj.modify()
print(obj.value) # Output: 21


