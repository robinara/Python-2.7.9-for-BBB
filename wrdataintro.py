import os

if os.path.exists('data.txt'):
    f = open('data.txt', 'a')
    print('Append to file.')
else:
    f = open('data.txt', 'w')
    print('Create new file.')

print('Writing...')
for x in range(1, 6):
    print(x)
    s = str(x) + '\n'
    f.write(s)

f.close()

print('Reading...')
fnew = open('data.txt', 'r')
print(fnew.read())
fnew.close()
