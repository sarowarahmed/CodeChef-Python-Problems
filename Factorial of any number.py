#Write a program that does the following

#Declare an integer variable num and initialize it to a user defined input
#Output to the console the factorial of num
#Remember to use loops for this problem
#Factorial of a number n is the product of all the numbers from 1 to n
#Factorial of a number(n) = n × (n-1) × ... 2 × 1

n=int(input("enter the number: "))
facto=1
for i in range(1,(n+1)):
    facto=(facto*i)

print(f"factorial of {n} is {facto}")  