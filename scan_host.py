import socket,sys
import time
from thread_test import MyThread

socket.setdefaulttimeout(1)
thread_num=4
ip_end=256
ip_start=0
#port = 22
scope=ip_end/thread_num


def scan(ip_head,ip_low, port):
    try:
        # Alert !!! below statement should be inside scan function. Else each it is one s
        ip=ip_head+str(ip_low)
	print ip
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
        s.close()
	print "ip %s port %d open\n" %(ip,port)
        return True
    except:
        return False


def scan_range(ip_head,ip_range,port):
	start,end=ip_range
	for i in range(start,end):
		scan(ip_head,i,port)

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
if len(sys.argv)<3:
	print "input ip and port"
	exit()

ip_head=sys.argv[1]
print type(ip_head)


port=int(sys.argv[2])
print type(port)

ip_range=[]
for i in range(thread_num):
	x_range=[i*scope,(i+1)*scope-1]
	ip_range.append(x_range)
#print ip_range

threads=[]
for i in range(thread_num):
	t=MyThread(scan_range,(ip_head,ip_range[i],port))
	threads.append(t)
for i in range(thread_num):
	threads[i].start()
for i in range(thread_num):
	threads[i].join()





'''
threads=[]
def test_fun():
	print "Test"
for i in range(20):
	t=MyThread(test_fun,())
	threads.append(t)

for i in range(20):
	threads[i].start()


for i in range(20):
	threads[i].join()



time.sleep(3)
'''


print "*****end*****"
