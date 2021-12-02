#!/usr/bin/env python3

with open("day2.txt") as f:
    data = f.read().splitlines()

position = { 
             "up": 0,
             "down": 0,
             "forward": 0
           }

for movement in data:
    action = movement.split()
    position[action[0]] += int(action[1])

print(position["forward"] * (position["down"] - position["up"]))

position = { 
             "horizontal": 0,
             "depth": 0
           }

aim = 0
for movement in data:
    direction, size = movement.split()
    size = int(size)

    if direction == "up":
        aim -= size
    elif direction == "down":
        aim += size
    else:
        position["horizontal"] += size
        if aim != 0:
            position["depth"] += size * aim

print(position["depth"] * position["horizontal"])
