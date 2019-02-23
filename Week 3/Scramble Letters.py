
import random


word_str = input("Enter a word: ")

length = len(word_str)


i = random.randint(1,length-2)
j = random.randint(1,length-2)

while i > j:
    print("i was bigger than j")
    i = random.randint(1, length - 2)
    j = random.randint(1, length - 2)


print(word_str)
new_str = word_str[:i] + word_str[j] + word_str[i+1:j] + word_str[i] + word_str[j+1:]

print(new_str)


