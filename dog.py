class Dog:
    
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = 3


    def __str__(self):
        return "{} is a {} dog {} years old weights {} pounds".format(self.name, self.sex, self.age, self.weight)

    #for intereactive 
    def __repr__(self):
        return self.__str__()    

    def eat(self):
        self.weight += 2

    def play(self):
        self.weight -= 1     

