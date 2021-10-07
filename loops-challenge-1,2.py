
# Loops Assignment (Only use For Loop):
# Challenge #1: Iterate through every number in a list named my_list to separate out even and odd numbers.
# Identify possible outlier values as well. Outliers means, values greater than 90 in this list.

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

evenNum = []
oddNum  = []
# outliers = [] is not find

for i in range(len(my_list)):
    if(i%2 ==0):
        evenNum.append(i)
    else:
        oddNum.append(i)
print("Even Num", evenNum)
print("Odd Num", oddNum)


# Challenge 2: Calculate the cumulative sum of all elements in a list named my_list.

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
sum = 0

for i in my_list:
    sum = i + sum
    print (sum)

