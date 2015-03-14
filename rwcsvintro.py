import os
import csv

if os.path.exists('table.csv'):
	f = open('table.csv', 'a')
	print('Append to file.')
else:
	f = open('table.csv', 'w')
	print('Create new file.')

a = [ range(150, 161), range(160, 171), range(170, 181) ]
print('Writing...')
w = csv.writer(f, delimiter=',')
for row in a:
    w.writerows([row])

for row in a:
    print(''.join(str(row)))

f.close()

print('Reading...')
fnew = open('table.csv', 'r')
print(fnew.read())
fnew.close()
