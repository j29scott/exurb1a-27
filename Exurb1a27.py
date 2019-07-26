import random
import time
import string

hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
count = -16
#---    Functions    ---#
def counter(): #Returns the first 8 digits of each row, does not handle the colon.
    global count
    count += 16
    return (format(count, '08x'))

def centerpiece(): #Returns the 8 parts in the middle
    center=''
    for i in range(8):
        block = ''
        for j in range(4):
            block += random.choice(hex)
        center += block + ' '
    return(center)

def lnend(): #Returns the last 16 characters. ~60% periods.
    content=''
    for i in range(16):
        if random.random() < 0.35:
            content += random.choice(string.digits + string.ascii_letters + string.punctuation)
        else:
            content += '.'
    return(content)

#---    Execution    ---#
print("Auraxis:˜ drakfyre$ xxd dosbox-0.74.tar.gz")
while True:
    print(counter()+': '+centerpiece()+' '+lnend())
    time.sleep(0.03)
