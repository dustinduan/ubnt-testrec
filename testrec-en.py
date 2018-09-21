import time
import platform as pl
import os
str_add='-000000'
def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")

def sfis_time():
    return ("Date:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')

def config_update():
    if os.path.exists('config.txt'):
        with open('config.txt','r') as source:
            a,machine=source.readline().split(':')
            b,mo=source.readline().split(':')
            c,station=source.readline().split(':')
    else:
        machine=input("Please input the current test machine name(4 codes):")
        mo=input("Please input the MO(12 codes):")
        station=input("Please input the Test Station(3 codes):")
    return(machine.strip('\n'),mo.strip('\n'),station.strip('\n'))
outlist=['test.txt','//10.6.1.14/公用Public/test.txt','//10.6.1.14/Assembly Public/testrec/test.txt','d:/summery.txt']
machine,mo,station=config_update()
machine=machine.upper()
mo=mo.upper()
station=station.upper()
ts=input("Please input the test result to be recorded(PASS/FAIL):")
test_status='PASS' if ts[0] in ['p','P'] else 'FAIL'
out_file=machine+'.txt'
outlist.append(out_file)
while True:
    for i in [machine,mo,station]:
        print(i)
    mac1=input("Please Scan the DUT MAC:").upper()
    if len(mac1)<13:
        mac=mac1+str_add
    else:
        mac=mac1
    for i in outlist:
        try:
            with open(i,'a') as tar:
                tar.write(machine.strip('\n')+mo.strip('\n')+station.strip('\n')+test_status+mac+' '+sfis_time())
        except:
            pass
    clean_screen()
