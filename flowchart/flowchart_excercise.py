raining = True
umbrella = False


def wait_a_while():
    print("Wait a while")


def go_outside():
    print("Go outside")


cnt = 0
while raining and not umbrella:
    wait_a_while()
    cnt += 1
    if cnt >= 10:
        go_outside()
        break
        # umbrella = True
    elif not raining:
        go_outside()
    elif umbrella:
        go_outside()
