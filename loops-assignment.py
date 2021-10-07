
# Write a Python program to print all natural numbers in reverse (from 10 to 1). 

natualNum = int(input("Enter Number: "))
print("Natual number form", natualNum, "-1 in reversed")

while(natualNum >=1):
    print(natualNum, end = " ")
    natualNum = natualNum -1
print("\n")

# Write a Python program to find sum of all natural numbers between 1 to 10.
    
sumNatualNum = int(input("Enter Number: "))
print("Sum of Natual number form 1-", sumNatualNum)

sumNum = 0
for i in range(2,sumNatualNum):
    if(i < 10):
        sumNum = i + sumNum
        print(sumNum, end = " ")
print("\n")

# Write a Python program to print all even numbers between 1 to 100

evenNum = int(input("Enter Number: "))
print("Even number form 1-", evenNum)

for i in range(1,evenNum):
    if(i%2 ==0):
        print(i, end = " ")
print("\n")
        
# Write a Python program to find sum of all even numbers between 1 to 10

SumEvenNum = int(input("Enter Number: "))
print("Sum of Even number form 1-", SumEvenNum)

evenSum = 0
for i in range(1,SumEvenNum):
    if(i%2 ==0):
        evenSum = i + evenSum
        print(evenSum, end = " ")
print("\n")

# Write a Python program to print all odd numbers between 1 to 100.

oddNum = int(input("Enter Number: "))
print("Odd number form 1-", oddNum)

for i in range(1,oddNum):
    if(i%2 ==1):
        print(i, end = " ",)
print("\n")

# Write a Python program to find sum of all odd numbers between 1 to 10.
SumOddNum = int(input("Enter Number: "))
print("Sum of Even number form 1-", SumOddNum)

oddSum = 0
for i in range(1,SumOddNum):
    if(i%2 ==1):
        oddSum = i + oddSum
        print(oddSum, end = " ")
print("\n")

# Write a Python program to print multiplication table of any number.
# e.g. Print the table for 2 in the following manner:

multiplicationNum = int(input("Enter the number of which the user wants to print the multiplication table: "))
print("MultiplicationNum table of ", multiplicationNum)

for count in range(1,11):
    print (multiplicationNum, 'x', count, '=', multiplicationNum * count)    

