# def test(x,y)
#    return x+y 
# test (10,20)

#time = input ("Enter time :")
#name = input ("Enter Name:")
#print ("Good afternoon" if time == "afternoon" else "good morning", end=" " )
#print(f"{name}")

def greeting(name,time):
    if time =="morning":
        print ("Good Morning")
    elif time == "afternoon" :
        print ("Good afternoon")
    elif time == "evening":
        print ("Good evening")    
    else :
        print ("Good Night")       
    return f"{name}"


name = input("Enter name : ")
time = input("Enter time:")
print (greeting(name ,time)) 