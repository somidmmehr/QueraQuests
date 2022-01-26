# !/usr/bin/env python3
"""
    QueraQuests: Chamran
    Author: SOMM
    Create date: 1400/11/04
"""
import sys
u_input = []

input_line = sys.stdin.readlines()
for x in input_line:
    for y in x.replace('\n', '').split(" "):
        u_input.append(int(y))

n = u_input[0]
a = u_input[1:]

if min(a) > n:
    print("YES")
else:
    if len(set(a)) == len(a):
        print("YES")
    else:
        if sum(range(n+1)) > sum(a):
            print("NO")
        else:
            b = {(x, a.count(x)) for x in a if a.count(x) > 1}
            check = True
            for (r, i) in b:
                if r+1 < i:
                    check = False
            if check:
                print("YES")
            else:
                print("NO")
