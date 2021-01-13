message = 'Hello World'

#printing the message.
print(message)

#Double quote
#if there is a quote in the string then better to use double quote to enclose the string.
message_withQuote = "Sam's World"
print(message_withQuote)

#Multiline Quote - using three quotes
message_MultilineQuote = '''Hello Sam, this is the long
multiline message , which can
be written by wrapping the message
within the triple quotes'''
print(message_MultilineQuote)

#trying multiline using \
message_MultilineQuote = '''Hello Sam, this is the \ 
long multiline message , \ which can
be written by wrapping \ the message
within the triple quotes'''
print(message_MultilineQuote)


#finding the length of the message - len()
print(len(message))

#finding character at particular index.
#string index starts from 0.
print(message[0])#first index value H
print(message[10]) #last index value d

#Slicing of string.
print(message[0:5])#starts from 0 and stops to 5 excluding 5.
print(message[0:11])#full string. It doesn't include the last index 11 instead till 10.

#Uppercase and Lowercase
print(message.lower())#all lower
print(message.upper())#all upper

#count the characters
print(message.count('l'))#count all characters 'l' in message 'hello world'

#To find the index of a character.
print(message.find('World'))#world starts at 6th index if not found returns -1.

#Replace method
message = message.replace('World','Universe')
print(message)

#adding the string or concat
greeting = 'Hello'
name = 'Michael'

#message = greeting +', ' + name + '. Welcome!' 

#Formatted string.
#message = '{}, {}. Welcome!'.format(greeting,name)

#Python 3.6 and above can use 'f string'
#can use "F" or "f" in the beginning.
message = F"{greeting}, {name}. Welcome!"

print(message)

#Shows all attribute and methods of string.
#print(dir(name))

#Gives all the description of string attributes and methods

#print(help(str))

#if we want particular attribute or method.
#print(help(str.count))


