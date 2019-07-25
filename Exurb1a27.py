import random
import time

a = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
b = 1
nukes = 0
while nukes == 0:
    if b < 10:
        c = "00000" + str(b)
    elif b < 100:
        c = "0000" + str(b)
    elif b < 1000:
        c = "000" + str(b)
    elif b < 10000:
        c = "00" + str(b)
    elif b < 100000:
        c = "0" + str(b)
    print(c," : ",a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)],a[random.randint(0,15)])
    b += 1
    time.sleep(0.06)
    if b > 9999999:
        print("run genocide.exe")
        time.sleep(3)
        print("Ah christ, turn the simulation off. This one's power mad as well. Delete it. Try 28 instead,  maybe the next one won't try to blow us up")
        nukes = 1