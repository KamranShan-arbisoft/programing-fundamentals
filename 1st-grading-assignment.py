
print("Enter Marks Obtained in 3 Subjects: ")
english = int(input())
math = int(input())
computer = int(input())

sum = english + math + computer
average = sum/3

if(average >= 90 and average <= 100):
    print("Your Grade is A")

elif(average >= 80 and average < 90):
    print("Your Grade is B")
    
elif(average >= 70 and average < 80):
    print("Your Grade is 3")

elif(average >= 60 and average < 70):
    print("Your Grade is D")
    
elif(average >= 50 and average < 60):
    print("Your Grade is E")
    
else:
    print("Your Are Fail")