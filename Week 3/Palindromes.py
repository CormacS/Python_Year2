#  Author: Cormac 'The Cool' Smith
import string

word_str = input("Enter a sentence: ")
bad_chars = string.whitespace + string.punctuation  # making a string with whitespace and punctuation in the same one

word_str = word_str.lower()  # Removes UpperCase Letters

for i in bad_chars:
    word_str = word_str.replace(i, "")  # For loop that will remove whitespace and punctuation


backwards_str = word_str[::-1]  # inverse of the string now that all the extra stuff has been removed


print("You Entered:\n", word_str)
print("\nBackwards that is:\n", backwards_str)

if backwards_str == word_str:   # Checks if the word and the word backwards are the same
    print("\nIt's a Palindrome!")
else:
    print("\nIt's not a Palindrome")


