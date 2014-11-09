import time
import os
from os.path import join
from time import mktime
from datetime import datetime

list_of_times = []
path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src'))
file = 'uga_7'
with open(join(path,file+".log"), "r") as reader:
    for line in reader:
        line = line.strip().split(',')
        #print line[0]
        list_of_times.append(time.strptime(line[0], "%Y-%m-%d %H:%M:%S"))

init_time = datetime.fromtimestamp(mktime(list_of_times[0]))
sum = 0
counter = 0
with open('uga.csv','a') as writer:
    for time_from_list in list_of_times[1:]:
        present = datetime.fromtimestamp(mktime(time_from_list))
        diff = present - init_time
        #if diff.total_seconds() < 100:
        #print diff.total_seconds()
        # if diff.total_seconds()<1000:
        #     print diff.total_seconds()
        #     sum += diff.total_seconds()
        #     counter += 1
        init_time = present
        writer.write("%s,%d\n"%(str(time_from_list),diff.seconds))
# average = sum / counter
# print average

