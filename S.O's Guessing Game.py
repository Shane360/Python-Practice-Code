import random
print('Hello, friend. What is your name?')
name = input()
secretNumber = random.randint(0, 10)
print('Welcome ' + name + '. Lets play a game. I am thinking of a number between 1 and 10. Guess which it is.')

print('The secret number is ' + str(secretNumber))     #Print the answer before user guesses
for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
            print('Your guess is too low.')
    elif guess > secretNumber:
            print('Your guess is too high')
    else:
            break

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed ' + str(guessesTaken) + ' times!')
else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))
