# 4 layer photos & storage
print('# 4. layer photos & storage')
for x in range(5):
    L = x + 1;
    for y in range(12):
        P = y + 1;
        photo = 'L' + str(L) + 'P' + str(P) + '.jpg';
        print('taking and storing photo ' + photo + ':\t');
    print('--- copying layer ' + str(L) + ' to windows')