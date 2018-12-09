#!/usr/bin/python3
import sys

def read_file():
    read_file = open('Zad_1.txt','r')
    read_text = read_file.read()
    print("\nRead text from file text.txt")
    print(read_text)

def write_file():
    print("Write text to file text.txt")
    text = sys.stdin.readline()
    file = open("text.txt","w")
    file.write(text)
    file.close()

read_file()

write_file()

read_file()


