import time
i = 0
while True:
    print("Hello")
    i = i + 1
    time.sleep(i)
    if i > 3:
        print("End of Loop")
        break
