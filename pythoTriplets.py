while True:
    sides = []
    for i in range(0, 3):
        sides.append(int(input('Enter the side length : ')))
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print('Pythagorean Triplets')
    else:
        print('Not Pythagorean Triplets')
    cont = input('press e to exit...')
    if cont == 'e':
        break
