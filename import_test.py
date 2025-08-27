import socket
hostname=socket.gethostname()
ipaddr=socket.gethostbyname(hostname)
print("Your computer name is: "+hostname)
print("Your ip address is: "+ipaddr)
'''
import time
current_time = time.localtime()
print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S", current_time))
custom_time = time.struct_time((1986, 7, 9, 0, 0, 0, 0, 190, -1))
print("Custom time:", time.strftime("%Y-%m-%d %H:%M:%S", custom_time))
'''