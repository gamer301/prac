# Python code to demonstrate
# how parent constructors are called.
	
# parent class
class Person( object ):	
	
		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):	
				self.name = name
				self.idnumber = idnumber
				
		def display(self):
				print(self.name)
				print(self.idnumber)
	
# child class
class Employee( Person ):			
		def __init__(self, name, idnumber, salary):
				self.salary = salary
	
				# invoking the constructor of
				# the parent class
				Person.__init__(self, name, idnumber)
		
		def show(self):
			print(self.salary)
			

class Employee2( Person ):			
		def __init__(self,salary, name="null2", idnumber=00 ):
				self.salary = salary
				super().__init__(name, idnumber)
				# invoking the constructor of
				# the parent class
				#Person.__init__(self, name, idnumber)
                
		
		def show(self):
			print(self.salary)
			print(self.name)  
			print(self)        
	
					

b =  Person ("pri",301)
c = Employee2(32)	

b.display()
c.display()
c.show()
