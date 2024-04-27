import random
choices = ['rock','paper','scissor']
while True:
    p1 = input('Enter your choice\t').lower()
    if p1 in choices:
     pass
    else:
     p1 = input('Enter a valid choice').lower()
    p2 = random.choice(choices)
    print("Your choice is "+ p1 +" and the other choice is "+p2)
    if p1 == p2:
      print("both players chose {p1}. It's a Tie")
    elif p1 == 'paper' and p2 == 'rock':
         print('p1 wins')
    elif p2 == 'paper' and p1 == 'scissor':
          print ('p1 wins')
    elif p1 == 'rock' and p2 == 'scissor':
          print('p1 wins')
    else :
          print('p2 wins')
    Restart = input('Do you want to play again y/n:').lower()
    if Restart != 'y':
       print('Thanks for playing')
       break
