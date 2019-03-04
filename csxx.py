# 变量信息
import string
import random
def INT():
     num=random.randint(0,999)
     return num

def FLOAT():
     fl=random.uniform(0,999)
     fln=round(fl,2)
     return fln

def UPPERCASE():
     S= string.ascii_uppercase
     R= random.choice(S)
     return R

def LOWERCASE():
     s=string.ascii_lowercase
     r=random.choice(s)
     return r

def FH():
     seed = "~!@#$%^&*()-_=+[]{},.?"
     fh=random.choice(seed)
     return fh

def ZFC():
     zfc = ''.join(random.sample(string.ascii_uppercase+string.ascii_lowercase+string.digits+'~!@#$%^&*()_-+=[{]}?', 8))
     return zfc

# def GB2312():
#     head = random.randint(0x4E00, 0x9FA5)
#     return head