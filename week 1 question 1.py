A=[5,3,8,6,1,9,2,7] #Array of integers
import random #Importing random for the randint function

i = 0
for i in range (8): #For loop will keep running through eight times as there are eight integers in the array
    j = random.randint(0,7) #Using randint gives a random number from the array between 0 and 7
    A[i] = A[j] #Now swapping the numbers that are now in i and j

print (A)
