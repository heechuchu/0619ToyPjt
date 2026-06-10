import random

answer = random.randint(1, 100)

while True:
    user = int(input("숫자 입력: "))

    if user > answer:
        print("DOWN")
    
    elif user < answer:
        print("UP")
    
    else:
        print("정답!")
        break