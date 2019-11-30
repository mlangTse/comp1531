'''
1. added two functions in class student, and added '__' at the front of 
the variable name, and make name unqiue for this class
2. added a import datetime, so that i can get the current year
in order to calculate the age, and it won't be break
'''
from datetime import datetime as dt
class Student:
    def __init__(self, firstName, lastName, birth_year):
        self.__name = firstName + " " + lastName
        self.__birth_year = birth_year

    def getName(self):
        return self.__name

    def getBirthyear(self):
        return self.__birth_year

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    now = dt.now().year
    years_old = now - s.getBirthyear()
    print(f"{s.getName()} is {years_old} old")
