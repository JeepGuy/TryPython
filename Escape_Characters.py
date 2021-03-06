# Escape Characters
# JCBrent
#
# The following is a code hack to eliminate ASCii encoding errors if in a foreign country
# -*- coding: utf-8 -*-

print("Escape Characters in Python")
print("----------------------------\n")
print("\\r   # Carriage return escape")

print('Note: the octothorpe "#" (hash or mesh) character is for comments - almost an escape character if you think about it.\n\n')

x_backslash = "\\\\"

print("The backslash character is escaped by typing a slash in front of it, as in {0} \n".format(x_backslash))    # py2.7 format (%s) \n" 	% x_backslash)

print("The backslash character is escaped by typing a slash in front of it, as in %s using the raw string = percent s \n" % x_backslash)

y_single_quote = "(\\')" 

print(" \\' = single quote escape %s  \n"% y_single_quote)


print(" \\a = the ASCii bell (BEL) character escape\n")

print(" \\b = the backspace escape character \n")

print(' \\f = the form feed escape character ')
print(" The form feed isn't used in Python - if importing data from another language this might be needed \n")

print(" \\n = the new line escape character (preferred over form feed in Python) ")

print(" \\N{name} = the Unicode database character escape  in Py2.7\n")


print(" \\r = carriage return escape character - not used in Python... \r")
print(" The carriage return isn't used in Python - instead Python uses a single line return \n")

print(" \\t = horizontal tab character escape character \n")

print(" \\uxxxx = 16bit Hex value escape character - Unicode only  \n")

print(" \\Uxxxxxxxx = 32 bit Hex value escape character - Unicode only \n")

print( " \\v = the verticle tab character escape character \n")

print (" \\ooo = the Octal character escape character with the value ooo \f")

print (" \\xhh = the Hex value escape character with the value of hh \n")

# -------------

print('Set the message variable equal to any string containing a new-line escape sequence')
message = "One\ntwo"
print(message);     print()

print('Add a string to the mountains variable that when printed results in: /\/\/\ ')
print('You will need to use an escape sequence more than once!')

mountains = "/\\/\\/\\"

print(mountains);    print()


print('Set the quotation variable to any string that contains an escaped double quotation mark \n')

quotation = "Time\'s up"

print(quotation)





