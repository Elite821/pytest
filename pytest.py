import time
tim1= 0
tim2= 0
min1= 0
min2 = 0
while True:
    tim1 = tim1 + 1
    time.sleep(1)
    if tim1 == 10:
        tim1 = 0
        tim2 = tim2 + 1
    if tim2 == 6:
        min1 = min1 + 1
        tim2 = 0
        tim1 = 0
    if min1 == 6:
        min2 = min2 + 1
        min1 = 0
        tim1 = 0
        tim2 = 0
    print(min2,min1,":",tim2,tim1)
