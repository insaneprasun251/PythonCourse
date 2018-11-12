import screeninfo

monitor_list = screeninfo.get_monitors()
# print(monitor_list[0])

print("Width: " + str(monitor_list[0].width) + " Height: " + str(monitor_list[0].height))