# coding=utf-8
import random

Game_Len = 4
colors = {
    1: "red",
    2: "blue",
    3: "green",
    4: "yellow",
    5: "white",
}
initial = []

while len(initial) < Game_Len:
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)
initial = [colors[i] for i in initial]
# print(initial)
win = False
for turn in range(3):
    guess = input()
    guess = guess.split(",")

    black = 0
    white = 0
    for i in range(len(guess)):
        if initial[i] == guess[i]:
            black += 1
        elif guess[i] in initial:
            white += 1

    print("black is {} and white is {}".format(black, white))
    if black == Game_Len:
        win = True
        print("you win")
if not win:
    print("You lose")
    print("initial state is {}".format(initial))