# !/usr/bin/env python3
"""
    QueraQuests: Bob and Remote control
    Author: SOMM
    Create date: 1400/11/04
"""
import sys
u_input = []

input_days = sys.stdin.readlines()
for x in input_days:
    for y in x.replace('\n', '').split(" "):
        u_input.append(y)

n_chanel = int(u_input[0])
start_chanel = int(u_input[1]) - 1
n_change_chanel = int(u_input[2])
channels = u_input[3:]

stop_channel = (start_chanel + n_change_chanel) % n_chanel

print(channels[stop_channel])
