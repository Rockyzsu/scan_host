import socket


socket.setdefaulttimeout(1)
port = 22


def scan(ip, port):
    try:
        # Alert !!! below statement should be inside scan function. Else each it is one s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False


'''
ip_start="10.19."
area=["133","134"]
for i in area:
    for j in range(255):
        ip_address=ip_start+i+"."+str(j)
        print ip_address
        result=scan(ip_address,port)
        if result :
            print "VNC" 
'''

for i in range(100,256):
    ip = "192.168.1." + str(i)
    #print ip
    if scan(ip, port):
        print "%s ssh" %ip
