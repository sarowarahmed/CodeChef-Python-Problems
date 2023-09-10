#Create a variable n and store the user defined input from console in n
#Output to the console the multiplication table for n upto 10
#In the previous module we manually entered each row of the table
#In this problem - use for loops to generate the table

n = int(input())
for i in range (1,11):
    print(n*i)