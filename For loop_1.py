#Write a program which does the following

#You are given a string containing some occurrences of the alphabet 'o'
#Count how many '0's are present in the string using a 'for' loop and 'if' condition

string = 'bolloon'
count = 0
for i in string:
    if i == "o":
        count += 1
print(count)        