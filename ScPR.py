from random import randint

COIN = ['Rock', 'Paper', 'Scissors']
ask = f"What's your choice? Print: Rock, Scissors or Paper"
print(ask)
n = input()
m = COIN[randint(0, 2)]
print(m)
if m == n:
    print("Draw")
if (m == 'Paper' and n == 'Rock') or (m == 'Rock' and n == 'Scissors') or (m == 'Scissors' and n == 'Paper'):
    print("Comp is winner")
if (n == 'Paper' and m == 'Rock') or (n == 'Rock' and m == 'Scissors') or (n == 'Scissors' and m == 'Paper'):
    print("You are winner")