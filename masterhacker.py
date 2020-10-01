import time
import random
import os
import sys
import math
import socket
os.system('color 2')
target = ''
last = None
while target == '':
    target = input('Enter Target: ')
    if (len(target.split('.')) != 4):
        try:
            print("IP:",socket.gethostbyname(target))
        except:
            target = ''
            print('enter valid ip or URL')
os.system('ping ' + target)
print('\n')
for i in range(75):
    if (i < 50):
        if i == 49:
            sys.stdout.write("\033[F" + "\033[K")
            print(f'{pre} done \n')
        pre = 'Searching for insecurities...'
    else:
        pre = 'Initiating hack...'
    if (last == None or last == '\\'):
        sys.stdout.write("\033[F" + "\033[K")
        print(f'{pre} /')
        last = '/'
        time.sleep(.1)
    elif (last == '/'):
        sys.stdout.write("\033[F" + "\033[K")
        print(f'{pre} -')
        last = '-'
        time.sleep(.1)
    else:
        sys.stdout.write("\033[F" + "\033[K")
        print(f'{pre} \\')
        last = '\\'
        time.sleep(.1)
sys.stdout.write("\033[F" + "\033[K")
print("Initiating hack... done\n")
for i in range(101):
    sys.stdout.write("\033[F" + "\033[K")
    print(f'Hacking {target} {i}% ({"█" * math.floor(i/2)}{"." * math.ceil((100-i)/2)})')
    time.sleep(random.uniform(0, i/25))
print(f'Hack on {target} complete')
input()
