from random import randint
import time
import os

#cores 
red = "\033[1;91m"
blu = "\033[1;94m"
gre = "\033[1;92m"
yel = "\033[1;33m"
mag = "\033[1;95m"

def clear():os.system('clear')

print(f"{yel}Cyber Gay kkkkkkkkkkk")
time.sleep(0.6)
clear()

nm = input(f'{gre}Opaa Qual o seu nick???:  ')
print(f"{yel}Iai {nm}")
print(" ")

n = int(randint(0, 10))

p=0

t = 0

while p != n:

    p = int(input(f'{red}Digite um numero {nm}: '))

    t+= 1

    if p == n:

        print(f'{blu}Acertou placar {t}')

    elif p <n:

        print(f'{mag}Digite um numero maior: ')

    else:

        print(f'{gre}Um numero Menor!')
        print(f'{blu}Game Over :( ')
        print(" ")


        
