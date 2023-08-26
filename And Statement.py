#Write a program which does the following:

#Declare a variables a and initialise it to the values 15 
#Compute a is divisible by both 7 and 5
#Depending on the result above - output the following to the console
#The number is divisible by both 5 & 7
#The number is not divisible by both 5 & 7

a = 15

# a%7 returns the remainder when a is divided by 7
if (a%7 == 0) and (a%5 == 0):       
    print('The number is divisible by both 5 & 7')
else:
    print('The number is not divisible by both 5 & 7')