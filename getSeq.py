
import gzip
import sys

line = ''
tag = True


switch ={
    150 : gene,
    63 : score,
    64 : score,
    1 : changetag
}

def gene():
    print(2)
    
def score():
    print(1)

def changetag():
    global tag
    tag = False


with gzip.open('L:/Creation/melon-BZR1-3-bHLH/BZR1-3-1_FKDL210116444-1a_1.fq.gz', 'r') as f1, open('out_file.txt', 'w') as f2:
    while tag:
        print(1)
        switch.get(1)()
#     print(f1.readline().rstrip(). == 150)
#     while(len(line = f1.readline().rstrip()) == 150):
#         if f1.readline()
    
