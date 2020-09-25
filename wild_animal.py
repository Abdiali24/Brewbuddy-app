class wild_animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f'This animal is called {self.name} and it is {self.age} years old') 

    


lion = wild_animal('Leo', 200)
lion.speak()
rhino = wild_animal('Trevor', 2000)
rhino.speak()
       