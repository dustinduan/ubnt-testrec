import os
import time
import platform as pl

def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")

if os.path.exists('//10.6.1.14/公用Public/test.txt'):
    info_file='//10.6.1.14/公用Public/test.txt'
elif os.path.exists('//10.6.1.14/Assembly Public/testrec/test.txt'):
    info_file='//10.6.1.14/Assembly Public/testrec/test.txt'
else:
    info_file='test.txt'
while True:
    mac=input("请输入需要查询的MAC:").upper()
    with open(info_file,'r') as source:
        for eachline in source:
            if mac in eachline:
                print(eachline)
