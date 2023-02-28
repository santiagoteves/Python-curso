"""
    == equal to
    != not equal to
    > greater than
    < less than
    >= greater than or equal to
    <= less than or equal to

"""

tries = 0
guess = 0

while guess != 6 and tries < 6:
  guess = int(input('Guess the number: '))
  tries = tries + 1

if guess != 6:
    print("You ran out of tries")
else:
   print("You got it")
