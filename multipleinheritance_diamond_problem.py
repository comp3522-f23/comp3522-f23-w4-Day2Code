"""
This module showcases how to solve the diamond problem and reliably call
the methods in the parent class(es) using the super() method.
"""


class BaseClass:
    """
    The base class from which all other classes derive from.
    """

    def call_me(self):
        """
        Example method that is overridden in the child classes.
        """
        print(f"Base Class Method executed")


class LeftSubClass(BaseClass):
    """
    LeftSubClass inherits from BaseClass and overrides the call_me
    method.
    """

    def call_me(self):
        """
        Overridden method from the BaseClass.
        """
        print(f"LeftSubClass Method executed")
        BaseClass.call_me(self)


class RightSubClass(BaseClass):
    """
    RightSubClass inherits from BaseClass and overrides the call_me
    method.
    """

    def call_me(self):
        """
        Overridden method from the BaseClass.
        """
        print(f"RightSubClass Method executed")
        BaseClass.call_me(self)


class ChildClass(LeftSubClass, RightSubClass):
    """
    ChildClass inherits from LeftSubClass and RightSubClass. This class
    overrides the call_me method found in both parents and the
    BaseClass.
    """

    def call_me(self):
        """
        Overrides the method with the same name found in BaseClass,
        LeftSubClass and RightSubClass.
        """
        print(f"ChildClass Method executed")
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)


def main():
    print("\nCall Me:")
    print("--------")
    test_object = ChildClass()
    test_object.call_me()


if __name__ == '__main__':
    main()
