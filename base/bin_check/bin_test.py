import random
import math

def int2bin(z):
    i = int(z)
    if i == 0: return "00000000"
    si = ''
    j = 1
    while (i > 0 or j < 9):
        if i & 1 == 1:
            si = "1" + si
        else:
            si = "0" + si
        i /= 2
        j += 1

    return si

def byte_write(fo):
    for k in range(0, 8):
        j = random.randint(0, 1)
        fo.write(str(j))
    fo.write('\n')
def byte_write1(fo):
    for k in range(0, 8):
        j = random.randint(0, 1)
        fo.write(str(j))

def x_init(s):
    f = open(s, "w")
    for i in range(0,20):
        f.write("d");f.write('\n')
    f.write("s")
    byte_write1(f);byte_write1(f);byte_write1(f);byte_write(f);
    for i in range(0, 223):
        f.write("v")
        byte_write1(f);byte_write1(f);byte_write1(f);byte_write(f);
    f.write("e")
    byte_write1(f);byte_write1(f);byte_write1(f);byte_write(f);
    for i in range(0,20):
        f.write("d");f.write('\n')
    f.close()

def z_init(s):
    f=open(s,"w")
    for i in range(0,141525):
        #byte_write1(f);byte_write1(f);byte_write1(f);byte_write(f);
        byte_write1(f);byte_write1(f);byte_write1(f);byte_write(f);
    f.close()


def a_init(s,weight):
    f=open(s,"w")
    if (weight>30):
        weight = 30
    elif (weight<0):
        weight = 0
    weight_c=30-weight
    for i in range(0,629):
        s=''
        j=random.randint(0,100)
        if (j==1):
            s="10000000000000000000000000000000" #ai=0
        else:
            l1=random.randint(0,1)
            s=s+"0"+`l1` #positive or negative ai
            l=random.randint(0,1)     #exponential value positive or negative
            if(l==0):
                for wei in range(0,weight_c):
                        s=s+"0"
            else:
                for wei in range(0,weight_c):
                        s=s+"1"

	    print(s)
            for k in range(0, weight):
                l = random.randint(0, 1)
                s = s + `l`
        f.write(s)
        f.write('\n')
    f.close()

sx = "test.bat" 
sz = "sz.bat"
sa = "sa.bat"
#x_init(sx)
#a_init(sa,24)
print(int2bin(1024))
