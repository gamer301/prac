class shape :
    def __init__(self,edge=1, shape="square" , color ="black" ):
        self.shape=shape
        self.color=color
        self.edge=edge 

    def details(self):
        print (self.shape, self.color)
        return self.shape,self.color 
    
    def area (self):
        print (self.edge**2)


class rectangle(shape):
    def __init__(self,length,breadth,shape="rectangle", color="black"):
        super().__init__(shape, color)
        self.length=length
        self.breadth=breadth
        print(shape,color,self.length,self.breadth)

    def area(self):
        print (self.length*self.breadth) 
        return self.length*self.breadth   
    
    def details(self):
        print (self.color)
        return self.color

class Triangle(shape):
    def __init__(self,base,height,shape="triangle", color="black"):
        super().__init__(shape, color)
        self.base=base
        self.height=height
        print(shape,color,self.base,self.height)

    def area(self):
        print("in area")
        print (0.5*self.base*self.height) 
        #return 0.5*self.base*self.height  
    
    def details(self):
        print (self.color)
        return self.color
    

tri=Triangle(3,1)
tri.area
tri.details

#rec=rectangle(length=3,breadth=5) 
#rec.area()       