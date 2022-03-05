import random
number = random.randint(1,10)

count = 0

while True :
    answer = input('請猜數字1 - 10: ')
    answer = int(answer)
    count += 1
    if answer == number :
        print('猜對了', number)
        print('猜了',count,'次')
        break
    elif answer > number :
        print('小於', answer)
    elif answer < number :
        print('大於', answer)
    else:
        print('請輸入數字')