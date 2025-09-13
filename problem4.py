class calculator:
    def __init__(self,n):
        self.n= n

    def square(self):
        print(f"The square of {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n*self.n*self.n}") 

    def squareroot(self):
        print(f"The squareroot of {self.n**1/2}")  

    @staticmethod
    def hello():
        print("hello how are you")           


p=calculator(4) 
p.hello()       
p.square()
p.cube()
p.squareroot()