#!/usr/bin/python3
import re

new_text=[]
file_name = input("Enter file name: ")

with open(file_name) as f:
	old_text = f.readlines()

for line in old_text:
	print(line)

for line in old_text:
	line = re.sub('i','oraz',line)
	line = re.sub('oraz','i',line)
	line = re.sub('nigdy','prawie nigdy',line)
	line = re.sub('dlaczego','czemu',line)
	new_text.append(line)

for line in new_text:
	print(line)




