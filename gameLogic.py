import random

wins = 0
again = True


print('\n')
print('═════════════════════════════════════════════════════════════════════════════')
print('✦ .  ⁺   . ✦ .  ⁺   . ✦  ROCK  ✦  PAPER  ✦  SCISSORS  ✦ .  ⁺   . ✦ .  ⁺   . ✦')
print('︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶')
print('\n')

while again==True:
    print('Welcome! Choose your fighter and have fun!')
    print('     1) Rock')
    print('     2) Paper')
    print('     3) Scissors')

    symbol = int(input('Enter a number: '))

    while symbol not in [1,2,3]:
        print('Sorry, invalid number!')
        symbol = int(input('Enter a number: '))

    print('\n')

    if symbol==1:
        print('You chose Rock')
    elif symbol==2:
        print('You chose Paper')
    else:
        print('You chose Scissors')

  

    computerSymbol = random.randint(1,3)

    if computerSymbol==1:
        print('The computer chose Rock')
    elif computerSymbol==2:
        print('The computer chose Paper')
    else:
        print('The computer chose Scissors')

    print('\n')

    if (symbol==1 and computerSymbol==3) or (symbol==2 and computerSymbol==1) or (symbol==3 and computerSymbol==2):
        wins+=1
        print('Congratulations, you won! (˶ᵔ ᵕ ᵔ˶) <3')
    elif symbol==computerSymbol:
        print('Oh no, a tie ( ˶°ㅁ°) !!')
    else:
        print('Sorry, you lost. (,,>__<,,)')

    print('\n')
    print(f'You already won {wins} times. Do you want to play again? \n         1) Yes\nAny Number) No')

    choice = int(input('Enter your choice: '))
    print('\n')
    if choice != 1:
        again = False



