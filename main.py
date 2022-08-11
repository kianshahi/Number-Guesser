import random
guess = random.randint(1,20)

print('Think of a number in your head and the computer will try to guess it! Once you see the guess, you can tell the computer if the guess was too high, too low, or correct')
print('The computer guesses ', guess) 
print('Enter h if the guess is too high')
print('Enter l if the guess is too low')
print('Enter c if the guess is correct')

while True:
    answer = input()
    if answer == 'c':
      print('I told you I knew what you were guessing!')
      break
    else:
      if answer == 'h':
        guess = int(guess) - random.randint(1,4)
        if int(guess) < 0: guess = 1
        print('The computer guesses ', int(guess))
        print('Enter h if the guess is too high')
        print('Enter l if the guess is too low')
        print('Enter c if the guess is correct')
      if answer == 'l':
        guess = int(guess) + random.randint(1,4)
        if int(guess) > 20: guess = 20
        print('The computer guesses ', int(guess))
        print('Enter h if the guess is too high')
        print('Enter l if the guess is too low')
        print('Enter c if the guess is correct')


