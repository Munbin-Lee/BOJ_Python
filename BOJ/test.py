import random

f = open("C:/Users/MB/Desktop/3.in", 'w')
f.write("1000\n")
for i in range(1000):
    n = random.randint(1, 1000000)
    f.write(str(n)+"\n")
f.close()
