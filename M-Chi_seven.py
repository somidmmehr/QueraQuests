# !/usr/bin/env python3
"""
    QueraQuests: چی سون؟
    Author: SOMM
    Create date: 1400/11/04
"""
import sys

holder = {}
line_n = 0

input_lines = sys.stdin.readlines()
for line in input_lines:
    line_n += 1
    if line_n == 1:
        continue
    if line[0:5] == "print":
        pindex = line.split(" ")[1].split("[")[0]
        in_pindex = line.split(" ")[1].split("[")[1]
        new_index = None
        if in_pindex[0] == "\"":
            new_index = str(in_pindex.replace("]", "").replace("\"", "").strip())
        else:
            new_index = int(in_pindex.replace("]", ""))
        print(holder[pindex][new_index])
    else:
        index, string_val = line.split(":=")
        index = index.strip()
        string_val = string_val.strip()
        if string_val[0] == "{":
            # is a dictionary
            in_dict = string_val.split(", ")
            new_dict = {kv.split(": ")[0].replace("\"", "").replace("{", ""): int(kv.split(": ")[1].replace("}", ""))
                        for kv in in_dict}
            holder[index] = new_dict
        else:
            # is a list
            in_list = string_val.split(", ")
            new_list = map(lambda x: int(x.replace("]", "").replace("[", "")), in_list)
            holder[index] = list(new_list)
