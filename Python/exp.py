class shape :
    def __init__(self, shape="square" , color ="black" ):
        self.shape=shape
        self.color=color 

class rectangle(shape):
    def __init__(self,length,breadth,shape="rectangle", color="black"):
        super().__init__(shape, color)
        self.length=length
        self.breadth=breadth
        print(shape,color,self.length,self.color)

    def area(self):
        print (self.length*self.breadth)    

rec=rectangle(length=3,breadth=5) 
rec.area()       