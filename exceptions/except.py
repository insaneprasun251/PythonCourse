from pip._vendor.distlib.compat import raw_input


def askint():
    while True:
        try:
            val = int(raw_input('Please enter an integer: '))
        except:
            print("Looks like you did not enter an integer")
            continue
        else:
            print("Correct")
            break
        finally:
            print("Finally block executed")
        print(val)

askint()