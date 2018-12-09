#!/usr/bin/python3
import os

def fun(tmp):
    count_of_directory = os.listdir(tmp)
    array = []
    for i in count_of_directory:
        path = os.path.join(tmp, i)
        if os.path.isdir(os.path.join(tmp,i)):
            array=array + fun(path)
        else:
            array.append(path)
    return  array           

path = input("Give a path:")
print (fun(path))
