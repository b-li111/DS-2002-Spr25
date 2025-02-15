#!/usr/bin/python3

import os

FAV_MONTH = input("What is your favorite month? ")
HOMETOWN = input("What is your hometown? ")
ONLY_CHILD = input("Are you an only child? ")

os.environ["FAV_MONTH"] = FAV_MONTH
os.environ["HOMETOWN"] = HOMETOWN
os.environ["ONLY_CHILD"] =  ONLY_CHILD

print(os.environ["FAV_MONTH"])
print(os.environ["HOMETOWN"])
print(os.environ["ONLY_CHILD"])
