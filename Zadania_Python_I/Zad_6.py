#!/usr/bin/python3
import os
import re

path = './'
jpg = '.jpg'
png = '.png'

def transformation(jpg_format, png_format):
    files = os.listdir(path)
    for i in files:
        extention = os.path.splitext(i)[1]
        if jpg_format == extention:
            new_extention = i.replace(jpg_format, png_format)
            os.rename(i, new_extention)

transformation(jpg, png)




