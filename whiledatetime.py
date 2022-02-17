import datetime
import os

start = datetime.datetime.now()
while True:
    print("현재 시간은 ",datetime.datetime.now())
    print("타이머는 : ", datetime.datetime.now() - start)
    os.system('cls')