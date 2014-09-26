import json
import time
import csv

min = 0
max = 0
with open("/Users/nilayan/Project/data/ukr_50k.txt","r") as r:
	reader = csv.reader(r)
	try:
		for row in reader:
			print row[0]
			ts = time.strptime(row[0],'%Y-%m-%d %H:%M:%S')
			print ts
			print min
			if min == 0:
				min = ts
				print "Min"
				print min
			else:
				if min>ts:
					min = ts
					print "Min"
					print min
			if max==0:
				max = ts
				print "Max"
				print max
			else:
				if max<ts:
					max = ts
					print "max"
					print max
	except ValueError:
		pass
	except IndexError:
		pass
	except Exception, e:
		pass