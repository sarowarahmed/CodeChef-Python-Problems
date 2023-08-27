#Write a program which does the following:
#Take input from the console for integer variables z, x and c
#Compute and output the following for each tuple z, x and c
#"PASS" if c is greater than either x or z
#Otherwise print "FAIL" in every other case

z, x, c = map(int, input().split())

# Update your code below this line to compare c with z and x
if c> x or c>z:
    print("PASS")
else:
    print("FAIL")