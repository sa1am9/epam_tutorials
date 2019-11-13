from sys import getsizeof
from random import random


f = open("test.txt", "w")
while getsizeof(f)<1000:
    f = open("test.txt", "w")
    print(getsizeof(f))
    f.write("csfdklbg;erhajonhbprsiwha;jerklgekru;gjikqrepoabj whdsgusdjg"+
            "sjadgoisajgoisdgjoimsdgansdaogio \n"+
            str(random()*1000000)+ " ")

