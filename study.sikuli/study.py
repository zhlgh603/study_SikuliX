import time

count = 0
day = 0
while 1 == 1:
    localtime = time.localtime(time.time())
    if 0 == day:
        day = localtime.tm_mday
    if (day <> localtime.tm_mday) and (1 == localtime.tm_hour):
        break   
    foundTicket = exists("1531221303190.png", 10) 
    print localtime
    if (None <> foundTicket) :
        print "foundTicket"    

        option = count % 4
    
        if (option == 0) :
            print "click A"
            click("1531233442101.png")
            
        elif (option == 1):
            print "click B"
            click("1531233458583.png")
            
        elif (option == 2):
            print "click C"
            click("1531233479568.png")
            
        elif (option == 3):
            print "click D"
            click("1531233493819.png")
            
        else:
            print "click A"
            click("1531233515423.png")
            

        wait("1531225947940.png")
        click("1531225980498.png")

        exists("1531234291257.png", 5)
            
        print "finish"