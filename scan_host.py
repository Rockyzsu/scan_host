import socket,sys
import time
from thread_test import MyThread

socket.setdefaulttimeout(1)

thread_num=4
 
ip_end=256
ip_start=0
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

if len(sys.argv)<3:
	print "input ip and port"
	exit()

ip_head=sys.argv[1]
port=int(sys.argv[2])


ip_range=[]
for i in range(thread_num):
	x_range=[i*scope,(i+1)*scope-1]
	ip_range.append(x_range)

threads=[]
for i in range(thread_num):
	t=MyThread(scan_range,(ip_head,ip_range[i],port))
	threads.append(t)
for i in range(thread_num):
	threads[i].start()
for i in range(thread_num):
	threads[i].join()
	

print "*****end*****"
