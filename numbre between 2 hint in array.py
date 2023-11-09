def inarray(t,n,m):
     a=[]
     for i in range(n,m):
        a.append(t[i])
     return a
while True:
   t=[]
   for i in range(10):
     R=int(input("type a numbre: "))
     t.append(R)
   n=int(input("type the first hint : "))
   m=int(input("type the second hint : "))
   print(inarray(t,n,m))
   p=input("do you want another list:(yes or no) ")
   if p=="no":
      break