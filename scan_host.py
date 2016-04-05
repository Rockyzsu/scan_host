import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(0.5)
port=5900
def scan(ip,port):
    try:
        s.connect((ip,port))
        return True
    except:
        return False

ip_start="10.19."
area=["133","134"]
for i in area:
    for j in range(255):
        ip_address=ip_start+i+"."+str(j)
        print ip_address
        result=scan(ip_address,port)
        if result :
            print "VNC"    
