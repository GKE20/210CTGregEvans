reverse_word = ''
a = input = ("This is awesome") #The inputted words to be reversed
for i in range(len(a), 0, -1): #For loop will run for the length of 'a' which is
                               #the inputted words then reverses the positions  
    reverse_word += a[i-1]     #this returns the reverse word plus 'a' which has
                               #now been reversed
print (reverse_word)


#The Big O notation run-time for this task is O(n). The reason it is O(n)
#is because of the one single for loop it contains, meaning it only has to run
#through the length of 'a' 



