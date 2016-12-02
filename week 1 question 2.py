def factorial (N):      #defining factorial function 
    s = 0
    for i in range (1, N+1): #For loop 
        while i > 0:    
            if i % 5 == 0:  #remainder division on the integer
                s += 1
                print (s)
                i = i/5
            else:
                break
    return s

print(factorial(5))        
