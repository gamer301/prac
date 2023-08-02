# def test(x,y)
#    return x+y 
# test (10,20)

#time = input ("Enter time :")
#name = input ("Enter Name:")
#print ("Good afternoon" if time == "afternoon" else "good morning", end=" " )
#print(f"{name}")

def binary(num):
    if num < 0 :
      return "Erorr"
    return bin(num)[2:] # we use [2:] to slice and start from 3rd element since python write 0b in front binary to diffrentiate 
    # we cal also use bin().replace("0b", "")

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


# name = input("Enter name : ")
# time = input("Enter time:")
# print (greeting(name ,time)) 

num = binary(int(input("Enter num for conversion :")))
print (num)

