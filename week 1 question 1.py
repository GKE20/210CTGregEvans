A=[5,3,8,6,1,9,2,7] #Array of integers
import random #Importing random for the randint function

i = 0
for i in range (8): #For loop will keep running through eight times as there are eight integers in the array
    j = random.randint(0,8) #Using randint gives a random number from the array
    A[i] = A[j] #Swapping the numbers that are i and j

print (A)
