class Student:
    "exercise 3"
    def __init__(self, name, matriNum, courses):
        self.name = name
        self.matriNum = matriNum
        self.courses = courses
        pass


s = Student("lcy", 123, "jjj")
print(s)