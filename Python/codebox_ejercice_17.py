"""
    == equal to
    != not equal to
    > greater than
    < less than
    >= greater than or equal to
    <= less than or equal to

"""

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

  if pin == 1234:
    print('PIN accepted!')