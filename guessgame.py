# guessing game
count=0
max_count = 3
secret_num = 6
while count < max_count: 
  userguess = input('Guess a secret number btw 0 to 9:')
  count += 1
  if int(userguess) == secret_num:
        print('You guessed right')
        break;
  else:
        print('Wrong! Take another guess')

print('Out of guesses')