# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

new_word = s[0:3] + t[4:]
print new_word




# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 

# ENTER CODE BELOW HERE

position = text.find("hoo")
print position




# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

#ENTER CODE BELOW HERE

first_occur = text.find("zip")

second_occur = text.find("zip", first_occur + 1)

print second_occur




# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159
#x = 6.849838
#ENTER CODE BELOW HERE

x = x + 0.5
string_x = str(x)
#print string_x

find_decimal = string_x.find(".")
#print find_decimal

round_up = string_x[0 :find_decimal]
print round_up
