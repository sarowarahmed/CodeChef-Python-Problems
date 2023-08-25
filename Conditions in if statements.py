#Write a program which does the following:
#Task-1

#Take input from the console for integer variables a and c.
#Compute and output the following for each pair a and c
#"Bravo!" if a is greater or equal to c
#Otherwise print "Try again" in every other case

a, c = map(int, input().split())      # Will cover this syntax for accepting multiple inputs later

# Update the code below this line to complete Task 1
if a>=c:
    print("Bravo!")
else:
    print("Try again")
