# This program is a game of hangman using strings

correct_str = 'guiness'
length = len(correct_str)
lives = 10

secret_str = '*' * length

print(secret_str)

while lives != 0:
    guess = input('Guess a letter' + '\n')

    if guess in correct_str:
        i = 0
        while i < length:
            if guess == correct_str[i]:
                secret_str = secret_str[:i] + correct_str[i] + secret_str[i+1:]
                i = i + 1
            else:
                i = i + 1
    else:
        print('That Letter is incorrect')
        lives = lives - 1
        print('You now have ' + str(lives) + ' lives left')

    print(secret_str)

    if secret_str == correct_str:
        print('You win!')
        break

if lives == 0:
    print('You lose, the word was :', correct_str)





