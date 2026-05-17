import python_module_library as mdl
from random import randint


#print(mdl.sum_value(1, 2, 3))
#print(dir(mdl))

MAX_RETRY = 10
NB_DASH = 50
lotteryValue = randint(1, 50)

i=1
while(i <= MAX_RETRY):
    mdl.clear_screen()
    mdl.displayWelcomeMessage(NB_DASH)

    if(i < MAX_RETRY):
        print (f"\nYour ({i}) attempt ")
    else:
        print(":) This is your last chance to try")

    while True:
        guestValue = input("Guest number from 1 to 50 : ")
        try:            
            guestValue = int(guestValue)
            break
        except ValueError:
            print("Only inter value is accept")

    if (guestValue < lotteryValue ):
        print(f"Value you guest [{guestValue}] is smaller than expected] ")
    elif (guestValue > lotteryValue ):
        print(f"Value you guest [{guestValue}] is bigger than expected] ")
    elif (guestValue == lotteryValue):
        print("You win.")
        break

    mdl.pause_for_action()
    i +=1


