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

#using lower w/ find
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)

#a use of variables, .find, .lower, and adding a number var to a string var to find the position of
shift = 3

#finds the slot h(text[0].lower) within the alphabet var
index = alphabet.find(text[0].lower())
print(index)
#output = 7

shifted2 = alphabet[index]
print(shifted2)
#output = h

#adding 3 to find what is 3 slots over from shifted2
shifted = alphabet[index + shift]
print(shifted)
#output = k
































