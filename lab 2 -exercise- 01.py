


num = float(input('How much is your team favored:'))

home = input('Is it a (h/H)ome game:')
home_game = home == 'h' or home == 'H'

team = input('Are they the Bengals (y/Y):')
bengals = team == 'y' or team == 'Y'


if bengals:
    print('NO! NO! NO!')

elif num >= 7.5:
    print('SLAM IT!')

elif num >= 3:
    if home_game:
        print('Good bet')
    else:
        print('Okay bet')
elif num >= 0:
    if home_game:
        print('Highly risky')
    else:
        print("Don't bet!")

elif num <= 0:
    print("Don't bet!")
    




