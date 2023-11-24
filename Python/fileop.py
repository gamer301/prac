import pickle
try:
 with open ("game.dat",'rb') as f :
     l= [('a',100),('b',100),('b',400),('a',200),('b',100),('a',300)]
     #pickle.dump(l,f)
     #print (l)

     x=pickle.load(f)
     b=0
     for a in x:
        if a==x[a]:
           b+=b
     print(b)       


except:
   pass
