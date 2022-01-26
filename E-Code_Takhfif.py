# !/usr/bin/env python3
"""
    QueraQuests:    Given a string of acceptable characters,
                    return whether a given combination of character is using only those given characters at least once
    Author: SOMM
    Create date: 1400/11/04
"""
import sys
u_input = []

input_days = sys.stdin.readlines()
for x in input_days:
    for y in x.replace('\n', '').split(" "):
        u_input.append(y)

base_chars = u_input[1]
code_input = u_input[2:]
for code in code_input:
    if set(sorted(base_chars)) == set(sorted(code)):
        print("Yes")
    else:
        print("No")
