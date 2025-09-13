class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):   
        print(f"The values of TwoDvector = {self.i}i + {self.j}j")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):  
        print(f"The values of ThreeDvector = {self.i}i + {self.j}j + {self.k}k")



a = TwoDvector(2, 1)
a.show()  

b = ThreeDvector(1, 2, 3)
b.show() 
