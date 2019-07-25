import random
import time
import string

hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
for it in range(9999999):
    #line to be built up
    line = ""

    #7 digit counter
    line = str(it).zfill(7) + ": "

    #8 groups of 4 blocks of hex chars
    for i in range(8):
        block = ''
        for j in range(4):
            block += random.choice(hex)
        line += block + ' '
    
    line = line + "\t"

    #not entirely sure what last bit is...
    #roughly 50% '.' and 50% random ascii?
    #16 characters in a row
    for i in range(16):
        if random.random() < 0.25:
            line += random.choice(string.digits + string.ascii_letters + string.punctuation)
        else:
            line += '.'
    print(line)
    time.sleep(0.05)

#terminate 
print("run genocide.exe")
time.sleep(3)
print("Ah christ, turn the simulation off. This one's power mad as well. Delete it. Try 28 instead, maybe the next one won't try to blow us up")
