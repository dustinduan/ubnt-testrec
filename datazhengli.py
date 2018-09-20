import os
import shutil
def txt_compress(filename):
    df=[]
    with open(filename,'r') as source:
        for eachline in source:
            df.append(eachline)
    k=set(df)
    with open('temp.txt','w') as tar:
        for i in k:
            tar.write(i)
    f1=open('temp.txt')
    f2=open(filename,'w')
    shutil.copyfileobj(f1,f2)
    f1.close()
    f2.close()
    os.remove('temp.txt')
filelist=['test.txt','//10.6.1.14/公用Public/test.txt','//10.6.1.14/Assembly Public/testrec/test.txt','d:/summery.txt']
for i in filelist:
    if os.path.exists(i):
        try:
            txt_compress(i)
        except:
            pass
print('log文件压缩完成')
