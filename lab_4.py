def lab_4_1(bot, top):
    sum = 0
    for n in range (bot, top+1):
        if n % 2 == 0:
            sum = sum + n
    print (sum)
lab_4_1(2, 100)



def lab_4_2(bot, top):
    sum = 0
    for n in range (bot, top+1):
        if n**0.5 - int(n**0.5) == 0:
            sum = sum + n
    print (sum)
lab_4_2(1, 100)



def lab_4_3(bot, top):
    sum = 0
    for n in range (bot, top+1):
        sum = sum + n**2
    print (sum)
lab_4_3(0, 20)



def lab_4_4():
    sum = 0
    bot = int(input ("input bot:"))
    top = int(input ("input top:"))
    for n in range (bot, top+1):
        if n % 2 == 1:
            sum = sum + n
    print (sum)
lab_4_4()



def lab_4_5():
    sum = 0
    inp = input ("input a num:")
    for s in inp:
        n = int(s)
        if  n % 2 == 1:
            sum = sum + n
    print (sum)
lab_4_5()



def lab_4_6():

    haveodd = 0
    oddmax = 0
    inp = input ("input 10 int:").split(",")

    for l in inp:
        n = int(l)
        if n % 2 == 0 and haveodd == 0:
            haveodd = haveodd + 0
        if n % 2 == 1:
            if haveodd == 0:
                oddmax = n
                haveodd = haveodd + 1
            if n > oddmax:
                oddmax = n

    if haveodd == 0:
        print ("no odd number")
    if haveodd != 0:
        print (oddmax)

lab_4_6()



def lab_4_7():
    
    havenum = 0
    sum = 0
    inp = input ("input string:")

    for s in inp:
        tf = s.isdigit()
        if tf == True:
            havenum = havenum +1
            sum = sum + int(s)

    if havenum == 0:
        print ("no digit")
    if havenum != 0:
        print (sum)

lab_4_7()



def lab_4_8():
    sum = 0
    inp = input ("input string:").split(",")
    for s in inp:
        sum = sum + float(s)
    print (sum)
lab_4_8()
