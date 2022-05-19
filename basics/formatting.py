for i in range(1, 15):
    print('i: {0:2} i square {1:4}: i cube {2:4}'.format(i, i ** 2, i ** 3))

for i in range(1, 15):
    print('i: {0:2} i square {1:<4}: i cube {2:^4}'.format(i, i ** 2, i ** 3))

print()
print("PI: {:12}".format(22/7))
print("PI: {:12f}".format(22/7))
print("PI: {:<12f}".format(22/7))
print("PI: {:^12f}".format(22/7))
print("PI: {:12.50f}".format(22/7))
print("PI: {:62.54f}".format(22/7))
print(f'Pi: {22/7}')
print(f'Pi: {22/7:.50f}')
