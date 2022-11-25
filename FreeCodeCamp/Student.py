class Student:
    #initialize function
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = name
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa <= 1.5:
            return True
        else:
            return False