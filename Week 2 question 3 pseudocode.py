//Pseudocode

from math import *
def func HIGHEST PERFECT SQUARE (N)            //defining function
    A <- squareroot(N) //Square root of N (input number)
    B <- integer(A)    //Turning it to an integer becuase it could be a float because
                       //it won't always be a whole number and is likely to be a decimal
    C <- B**2         //Performs B to the power of 2 to get the closest whole number
                      //and square number
                      
    output ((str('')) + (str(C)))
HIGHEST PERFECT SQUARE(20)

