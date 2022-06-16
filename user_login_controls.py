
from sys import get_coroutine_origin_tracking_depth
from PySide2 import QtCore, QtWidgets, QtGui

# The reason to import this is because it was auto generated
from forms.ce_login_main import Ui_Main_window

class User_login_controls(QtWidgets.QWidget):

    def __init__(self, broker):
        super(User_login_controls, self).__init__()
        print("Nice  Alma!")
        self.broker = broker
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)

        #TODO: make the window show. 


        self.make_connections(self)

    def make_connections(self):
        # here is where you will make connections to the buttons and right click actions 
        # useful to look into how to connect actions to buttons (Hint: clicked.connect)
        # look into what lamda is in python
        pass

    def retranslateUi(self):
        self.ui.retranslateUi(self)

    def configure(self, source):
        pass

    def show_controls(self):
        pass

# def main():
#     qt_app = QtWidgets.QApplication
#     object1 = User_login_controls(qt_app)

# if __name__ == "__main__":
#     main()








# make a simple class test() that prints hello world in the __init__()
# inside the class make a mehtod(like function) called class_function_test() and print I got in here 


#in the main initialize that class and see what happens 
#  be able to print this class_function_test()




# class LessonPlan():
#     def __init__(self, subject):
#         self.subject = subject
#         print("I made a new object called learning")
#     def add_learning_objective(self):
#         print("I called a method of class learning!")

# def main():
#     print("start program")
#     math_lesson_plan = LessonPlan ("Math") #i initialized an instance of class (LessonPlan)
#     math_lesson_plan.add_learning_objective()

# if __name__ == "__main__":
#     main()


# class Country:
#     def __init__(self, name):
#         self.name = name
#         print("I'm from " + self.name)

# def main():
#     the_country__of_iran = Country("Iran")

# if __name__ == "__main__":
#     main()


# class IceCream:
#     def __init__(self, flavor):
#         self.flavor = flavor
        
#         print("I want " + self.flavor + " ice cream")

# def main():
#         flavor1 = IceCream("vanilla")
#         flavor2 = IceCream("chocolate")

# if __name__ == "__main__":
#     main()




class Coffee:
    type = ""
    coffee_prices = {
        "latte": 4.20,
        "cappuccino": 5.12,
        "esspresso": 3.14,
        "extra_shot": 0.5,
        "caramel_frappuccino": 6.34 
    }

    def __init__(self, type):
        self.type = type
        print("I want a " + self.type)
    
    def get_price(self):
        return self.coffee_prices[self.type]


def main():
    drink_1 = Coffee("latte")
    drink_2 = Coffee("cappuccino")
    print(drink_1.get_price())
    print(drink_2.get_price())

if __name__ == "__main__":
    main()
