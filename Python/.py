class vehicle :

  def __init__(self,capacity=4,color="White",fare=0) :
    self.capacity=capacity
    self.color=color
    self.fare = fare + capacity*100

veh1=vehicle()
print(veh1.capacity,veh1.color,veh1.fare)

class bus(vehicle):

  
  def __init__(self, capacity=50, color="Red",fare=0):
    self.cap_bus=capacity
    self.col_bus=capacity
    self.fare= fare+capacity*100
    print(self.fare) 
    self.total_fare= self.fare + ((self.fare /100)*10)

bus1=bus()
print(bus1.total_fare)



    