import random #Mertcan Yildirim 99068314
print('Je gaat een spel spelen waar je moet gokken') #Hoe maak je rondes en dat je 10 keer per ronde kan gokken en dat je elke ronde kan aangeven dat wilt gaan stoppen
teradengetal = random.randint(1,1000)
score = 0
ronde = 1
ready = input('Ben je klaar om te spelen? j/n ')
if ready == 'n':
    print('Bye!')
else:
    print('ronde:', ronde)
    geraden = False
    tries = 10
    while geraden == False or tries >0 or Doorgaan1 == 'j' or Doorgaan2 == 'j':
        gok = int(input('Gok een getal '))
        if gok != teradengetal:
            tries -= 1
        if tries == 0:
            Doorgaan1 = input('Helaas ben je gefaalt, doorgaan? n/j ')
            if Doorgaan1 == 'n':
                print('Bye!')
                break
            else:
                teradengetal = random.randint(1,1000)
                tries = 10
                ronde += 1
                print ('ronde:', ronde)
        if gok > teradengetal:
            print('Het getal is kleiner')
        elif gok < teradengetal: 
            print('Het getal is groter')

        if abs(gok - teradengetal) <20:
            print('Je bent heel warm!')
        elif abs(gok - teradengetal) <50:
            print('Je bent warm!')
        
        if gok == teradengetal:
            geraden = True  
        if geraden == True and tries >0:
            print('Gefeliciteerd u heeft het geraden!')
            score += 1
        print('Huidige score: ', score)
        if geraden == True:
            Doorgaan2 = input('Wil je nog doorgaan? n/j ')
            if Doorgaan2 == 'n':
                print('Bye!')
                break
            else:
                teradengetal = random.randint(1, 1000)
                tries = 10
                ronde += 1
                print ('ronde:', ronde)
            if ronde >20:
                print('Game Over! Huidige score:', score)
                break
