N=int(input())
l=input()
l2=l.split()
for x in l2 :
    if int(x) not in range (1,N+1):
        print (int(x))