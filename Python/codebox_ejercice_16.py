"""
    == equal to
    != not equal to
    > greater than
    < less than
    >= greater than or equal t\o
    <= less than or equal to 
    
"""

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Do you like Dawn or Dusk:")
print(" 1) Dawn")
print(" 2) Dusk")

question_1 = int(input("Choice 1 or 2: "))

            
if question_1 == 1:
    Gryffindor +=1
    Ravenclaw +=1
elif question_1 == 2:
    Hufflepuff  +=1
    Slytherin +=1 
else:
    print("Wrong input")


print("When i´m dead, I want people to remember me ass: ")
print(" 1) The Good")
print(" 2) The Great")
print(" 3) The Wise")
print(" 4) The Bold")

question_2 = int(input("Choice 1 or 2 or 3 ro 4: "))

if question_2 == 1:
    Hufflepuff+=1
elif question_2 == 2:
    Slytherin+=1
elif question_2 == 3:
    Ravenclaw+=1
elif question_2 == 4:
    Gryffindor+=1
else:
    print("Wrong input")

print("Which kind of instrument most pleases your ear? ")
print(" 1) The violin")
print(" 2) The trumpet")
print(" 3) The piano")
print(" 4) The drum")

question_3 = int(input("Choice 1 or 2 or 3 or 4: "))

if question_3 == 1:
    Slytherin+=1
elif question_3 == 2:
    Hufflepuff+=1
elif question_3 == 3:
    Ravenclaw+=1
elif question_3 == 4:
    Gryffindor+=1
else:
    print("Wrong input")


if Gryffindor >= Ravenclaw and Gryffindor >=  Hufflepuff and Gryffindor >= Slytherin:
    print("You are from Gryffindor")
elif Hufflepuff >= Ravenclaw and Hufflepuff >= Slytherin:
    print("You are from Hufflepuff")
elif Ravenclaw >= Slytherin:
    print("You are from Ravenclaw")    
else:
    print("You are from Slytherin")
