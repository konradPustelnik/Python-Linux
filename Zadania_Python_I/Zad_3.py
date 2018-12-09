#!/usr/bin/python3
import os

path="/dev"

def fun(tmp):
    directory = os.listdir(tmp)
    return  len(directory)

print (fun(path))
