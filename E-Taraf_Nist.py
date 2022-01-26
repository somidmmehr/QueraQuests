# !/usr/bin/env python3
"""
    QueraQuests:    Given an input of work shifts of a company's staff,
                    return the number of days no staff is present at the company
    Author: SOMM
    Create date: 1400/11/04
"""
import sys
WEEK_DAYS = {"shanbe",  "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"}
work_days = []

"""
# if the input is commandline:
try:
    n_days_staff1 = int(input("number of days staff 1 will be present at company: "))
    days_staff1 = input("days staff 1 will be present at company (separated by space): ")
    n_days_staff2 = int(input("number of days staff 2 will be present at company: "))
    days_staff2 = input("days staff 2 will be present at company (separated by space): ")
    n_days_staff3 = int(input("number of days staff 3 will be present at company: "))
    days_staff3 = input("days staff 3 will be present at company (separated by space): ")
    work_days = set(days_staff1.split(" ")+days_staff2.split(" ")+days_staff3.split(" "))
except Exception as err:
    print(err)
"""

"""
# if the input is a file named "input.txt" in the root folder of the project
try:
    with open("input.txt") as input_days:
        for x in input_days.readlines():
            for y in x.replace('\n', '').split(" "):
                work_days.append(y)
except Exception as err:
    print(err)
"""

# if it uses multiline to read the input:
input_days = sys.stdin.readlines()
for x in input_days:
    for y in x.replace('\n', '').split(" "):
        work_days.append(y)

answer = [free_day for free_day in WEEK_DAYS if free_day not in work_days]
print(len(answer))
