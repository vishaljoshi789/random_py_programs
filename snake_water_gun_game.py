import random        #module to generate ramdom things

def game(ySelect, cSelect):               #game function
    if ySelect == cSelect:
        return 'Both guess were same so its a TIE'    
    elif ySelect == 's' and cSelect == 'w':
        return 'YOU WON !!!'
    elif ySelect == 'w' and cSelect == 'g':
        return 'YOU WON !!!'
    elif ySelect == 'g' and cSelect == 's':
        return 'YOU WON !!!'
    else:
        return 'You Lose!!!'

# giving a random value to compter
print("-----------Its computer's turn-------------")
randNum = random.randint(1, 3)              # giving random value to cSelect
if randNum == 1:
    cSelect = 's'
elif randNum == 2:
    cSelect = 'w'
elif randNum == 3:
    cSelect = 'g'
print("----------Computer have chosen------------ ")

# user input
print("----------Its your turn---------------")
ySelect = input("What you wanna chose : type 's' for snake, 'w' for water, 'g' for gun --> \n")

# calling the function
a = game(ySelect, cSelect)
print(a)

# displaying the selected units
print(f'You chose {ySelect} and Computer chose {cSelect}')