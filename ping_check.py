import time
import os
import sys

ip_list = []
with open('/usr/ping_ip_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        ip_list.append(line.split(' ')[0])

# 循环ping
def circle_ping():
    start_time = time.strftime('%Y%m%d%H%M%S')
    with open('/usr/ping_result/ping_circle{0}.txt'.format(start_time), mode="a") as f:
        for ip in ip_list:
            ip = ip.split('\n')[0]
            #print(ip)

            ret = os.popen('ping -c 1 {0}'.format(ip)).read().split('% packet loss')[0].split(',')[-1].strip()
            #print(ret)

            if '100' in ret:
                ret_info = 'Failed!!!'.format(ip)
                #print(ret_info)
            else:
                ret_info = 'Success'.format(ip)
                #print(ret_info)
            info = '{0} - {1} - {2} - {3} \n'.format(ip, ret, ret_info, str(time.strftime('%Y-%m-%d %H:%M:%S')))
            print(info)
            f.write(info)

if __name__ == '__main__':
    circle_ping()
