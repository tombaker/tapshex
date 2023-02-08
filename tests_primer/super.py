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

if __name__ == '__main__':
    obj = ChildClass()
    obj.value = 10
    print(f"obj.modify().value: {obj.modify().value}")
    print(f"obj.value: {obj.value}") # Output: 21
    obj2 = ChildClass()
    obj2.value = 40
    print(f"obj2.modify().value: {obj2.modify().value}")
    print(f"obj2.value: {obj2.value}") # Output: 21
