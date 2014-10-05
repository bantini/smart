import time
from time import mktime
from datetime import datetime
list_of_times = []
with open("ukraine.log","r") as reader:
	for line in reader:
		line = line.split(',')
		list_of_times.append(time.strptime(line[0],"%Y-%m-%d %H:%M:%S"))

init_time = datetime.fromtimestamp(mktime(list_of_times[0]))
sum = 0
counter = 0
for time_from_list in list_of_times[1:]:
	present = datetime.fromtimestamp(mktime(time_from_list))
	diff = present-init_time
	if diff.total_seconds()<100:
		sum+=diff.total_seconds()
		counter+=1
	init_time = present

average = sum/counter
print average
	
