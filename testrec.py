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
        machine=input("请输入当前测试的机台编码(4位编码):")
        mo=input("请输入当前测试的12位工单号码:")
        station=input("请输入当前机种的测试站别(3位编码)")
    return(machine.strip('\n'),mo.strip('\n'),station.strip('\n'))
outlist=['test.txt','//10.6.1.14/公用Public/test.txt','//10.6.1.14/Assembly Public/testrec/test.txt','d:/summery.txt']
machine,mo,station=config_update()
machine=machine.upper()
mo=mo.upper()
station=station.upper()
ts=input("请输入需要记录的测试状态(PASS/FAIL):")
test_status='PASS' if ts[0] in ['p','P'] else 'FAIL'
out_file=machine+'.txt'
outlist.append(out_file)
while True:
    for i in [machine,mo,station]:
        print(i)
    mac1=input("请用扫描枪输入需要记录的产品MAC:").upper()
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
