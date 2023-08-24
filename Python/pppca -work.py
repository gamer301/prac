class shape :
    def __init__(self, shape="square" , color ="black" ):
        self.shape=shape
        self.color=color 

class rectangle(shape):
    def __init__(self,length,breadth,color,shape="rectangle"):
   #def __init__(self,shape="rectangle", color="white", length= 0 , breadth=0):
        super().__init__(shape, color) 
        self.length=length
        self.breadth=breadth
        print (self.length,self.breadth,shape,color)
        pass
    
    def area(x,y):
        area=x*y
        

class triangle(shape):
    def __init__(self, shape, color):
        super().__init__(shape, color)
    def area(b,h):
        area=0.5*b*h
#shape=shape("big long", "red")
sh=shape()
rec=rectangle(length=3 ,breadth=5)
#tri=triangle()        


