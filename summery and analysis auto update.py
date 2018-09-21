import platform as pl
import os
import time

def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")

if os.path.exists("//10.6.1.14/公用Public/test.txt"):
    sourcefile="//10.6.1.14/公用Public/test.txt"
else:
    sourcefile='test.txt'
def log_index(startnum=0,endnum=4):
    s=[]
    if os.path.exists("//10.6.1.14/公用Public/test.txt"):
        sourcefile="//10.6.1.14/公用Public/test.txt"
    else:
        sourcefile='test.txt'
    with open(sourcefile,'r') as source:
        for eachline in source:
            s.append(eachline[startnum:endnum])
        return(set(s))

machine=log_index()
mo=log_index(4,16)
station=log_index(16,19)
status=log_index(19,23)
while True:
    for x in mo:
        for y in station:
            for z in status:
                with open(sourcefile,'r') as source:
                    s=[]
                    for eachline in source:
                        if x in eachline and y in eachline and z in eachline:
                            s.append(eachline[23:42])
                k=set(s)
                n=len(k)
                print(x,y,z,n)
    time.sleep(30)
    clean_screen()
