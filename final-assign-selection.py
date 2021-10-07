
n = int(input("Please Enter your Number: "))

if(n%2 !=0):
    print("Not Weired")
    
elif(n>=2 and  n<=5):
    print("Weired")
    
elif((n>=6 and  n<=20) and (n%2 !=0)):
    print("Not Weired")  

else:
    print("Weired")