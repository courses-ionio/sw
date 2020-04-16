
import random
import sys

#Read number of generated random numbers as script argument
n = sys.argv[1]
afile = open(n+".txt", "w" )

for i in range(int(n)):
    line = str(random.randint(1, 1000000))
    afile.write(line)
    afile.write("\n")

afile.close()
