import time
import platform as pl
import os
bak_list=['//10.6.1.14/公用Public/test.txt','//10.6.1.14/Assembly Public/testrec/test.txt','d:/summery.txt']
for i in bak_list:
    try:
        with open('test.txt','r') as source:
            with open(i,'a') as tar:
                for eachline in source:
                    tar.write(eachline)
        print('下面的文件备份成功:',end=' ')
        print(i)
    except:
        print('下面的文件备份失败:',end=' ')
        print(i)
