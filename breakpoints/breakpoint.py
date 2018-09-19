def divide(e, f):
    try:
        # breakpoint()
        return f / e
    except ZeroDivisionError:
        print("ZeroDivision error occurred. Check values")


a, b = 0, 1
print(divide(a, b))
