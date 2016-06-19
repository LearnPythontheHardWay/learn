from sys import argv

script, first, second, third = argv
script = raw_input("The script is called:")
first = raw_input("Your first variable is:")
second = raw_input("Your second variable is:")
third = raw_input("Your third variable is:")

print "So, The script is called %r, Your first variable is %r, Your second variable is %r, Your third variable is %r." %(script, first, second, third)