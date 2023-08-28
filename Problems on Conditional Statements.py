#Write a program which does the following
#Make an auto-reply program that takes input from the user as an integer variable x
#Do the above for 2 separate input values
#x = 69
#x = 70
#Compute and output the following to the console
#Print "Order Confirmed" only if x < 70
#else Print "Order Limit reached"
#In both cases, the program must print "Thank YOU!" on a separate line.

x = int(input())
# Solution as follows

if x < 70:
    print("Order Confirmed")
else:
    print("Order Limit reached")
print("Thank YOU!")
    
    
    
x = int(input())
# Solution as follows for 2nd input

if x < 70:
    print("Order Confirmed")
else:print("Order Limit reached")
print("Thank YOU!")
