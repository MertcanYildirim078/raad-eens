import random
print('Je gaat een spel spelen waar je moet gokken') #Hoe maak je rondes en dat je 10 keer per ronde kan gokken en dat je elke ronde kan aangeven dat wilt gaan stoppen
teradengetal = random.randint(1,1000)
score = 0
ronde = 1
ready = input('Ben je klaar om te spelen? j/n ')
if ready == 'n':
    print('Bye!')
else:
    print('Ronde 1')
    geraden = False
    print(teradengetal)
    while geraden == False and tries <10:
        tries = gok == input
        gok = int(input('Gok een getal '))
        if gok > teradengetal:
            print('Het getal is kleiner')
        elif gok < teradengetal: 
            print('Het getal is groter')

        if abs(gok - teradengetal) <20:
            print('Je bent heel warm!')
        elif abs(gok - teradengetal) <50:
            print('Je bent warm!')
        if geraden == True or tries >10:
            ronde += 1
            stoppen = input('Wil je doorgaan? n/j ')
            if stoppen == 'n':
                print('Bye!')
            else:
                pass
        if ronde == 2:
            break 
        if gok == teradengetal:
            geraden = True  
        if geraden == True:
            print('Gefeliciteerd u heeft het geraden!')
            score += 1
        print(score)


    