"""Remove any given character from a string"""


def remove(string, char):
    return string.replace(char, "")


# Enter a string
string = input("Please enter a string : ")
# Enter a character to remove
char = input("Please enter a character to remove : ")
# Delete the character

print(remove(string, char))
