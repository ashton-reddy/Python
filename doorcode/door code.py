import msvcrt
import time

print("Beldum is blocking your path. Put in the code to move on. The code is 274. Please do not forget if you ever want move on. Beldum is nice and won't hurt you unless   you say the number 0 or 891+")
time.sleep(10)

print("Please enter your secret code")
x = msvcrt.getch()
y = msvcrt.getch()
z = msvcrt.getch()

while True:
    if (x == b'2' and y==b'7' and z==b'4'):
        print("Welcome to Metagross city")
        break
    bignumber = int(x+y+z)
    if (bignumber >= 891):
        print("beldum, use ")
        break
    x = y
    y= z
    z = msvcrt.getch()
