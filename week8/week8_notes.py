name = "juilet"

for ch in name:
    print(type(ch))

# len(string) can be used to obtain the amount of indicies in the string
for index in name:
    name[index] = name
print(name)

# mystring.method(arguments)
# isalnum()
# isalpha
# isdigit
# islower() # good for doing passwords checking if no uppercase are in
# isspace() returns t or f depending on white spaces
# isupper()

# .strip()
# lstrip() returns a copy of the string with all leading white spaces chars removed
# rstrip() returns a copy of the string with all trailing white chars removed.

# SUBSTRINGS:
# endswith(substring): checks if the string ends with 'substring'
# - returns t or f
# startswith(substring): checks if the string starts with a substring returns t or f
# find(substring): returns lowest index of the substring, or the substring is not contained in the string,
# returns -1
# replace(substring, new_string)
# split method which returns a list containing the words in the string
# - By default, uses space as seperator but you can add it in
# like split(", ") will determine what to split it on. anything depending on how the string is split up
# text files are always in strings. You have to convert them if you want to do any math with the values

my_string = "one two three four"
word_list = my_string.split()

password = input("Enter a password: ")
