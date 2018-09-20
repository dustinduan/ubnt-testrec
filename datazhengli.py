import os
def txt_compress(filename):
    df=[]
    with open(filename,'r') as source:
        for eachline in source:
            df.append(eachline)
    k=set(df)
    with open('temp.txt','w') as tar:
        for i in k:
            tar.write(i)
    os.remove(filename)
    os.rename('temp.txt',filename)
txt_compress('test.txt')
