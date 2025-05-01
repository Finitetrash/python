#this is a python file used for documenting our knowledge of python

#normal print command
print('why are you mean')

#finds character value of given variable
#finds character value of given variable and prints it under a new variable
spencer = 'loser'
hello = 'are you sure this works?'
index = print(hello.find(spencer[1]))
print(index)

#finds what is in slot six. you can use negatives to find charachters
t = 'Hello World'
print(t[6])

#finds the length of said string 
text = 'Hello World'
print(len(text))

#finds the type of code
print(type(text))

#how to use the .lower command to make all of ys lower case
ys = 'YOU SUCK'
print(ys.lower())

#finds the slot h(text[0].lower) within the alphabet var
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
#output = 7

#a use of variables, .find, .lower, and adding a number var to a string var to find the position of
shift = 3


shifted2 = alphabet[index]
print(shifted2)
#output = h

#adding 3 to find what is 3 slots over from shifted2
shifted = alphabet[index + shift]
print(shifted)
#output = k

#this is a for loop.
#it take 'chores' seperates the strings into 'chore' and then out puts it the amount of seperate stings that are in 'chores'

chores = ["wash dishes", "sweep floor", "take out trash"]

for chore in chores:
    print("I'm going to", chore)

#output
#I'm going to wash dishes
#I'm going to sweep floor
#I'm going to take out trash
































