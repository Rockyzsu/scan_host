import socket
import time
from thread_test import MyThread

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
'''
for i in range(1,256):
    ip = "10.19.134." + str(i)
    print ip
    if scan(ip, port):
        print "%s ssh open" %ip
'''
threads=[]
def test_fun():
	print "Test"
for i in range(20):
	t=MyThread(test_fun,())
	threads.append(t)

for i in range(20):
	threads[i].start()





time.sleep(3



print "*****end*****"
