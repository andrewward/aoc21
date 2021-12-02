#!/usr/bin/env python3

with open("day1.txt") as f:
    data = f.read().splitlines()

increases = 0
for i, line in enumerate(data):
    if i == 0:
        continue
    if int(line) > int(data[i-1]):
        increases += 1

print(increases)

increases = 0
data_len = len(data)
for i, line in enumerate(data):
    if i == data_len - 3:
        break
    splitl = int(line) + int(data[i+1]) + int(data[i+2])
    splitr = int(data[i+1]) + int(data[i+2]) + int(data[i+3])

    if splitr > splitl:
        increases += 1

print(increases)
