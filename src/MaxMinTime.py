import os
import time
import logging
from os.path import join
#_author__ = 'nilayan'

def MaxMinTime(f):
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    logging.basicConfig(filename = "out.log",format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    with open(join(path,f)) as reader:
        counter = 0
        min_time = None
        max_time = None
        for line in reader:
            try:
                time_file = line.split(",")[0]
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(time_file,'%Y-%m-%d %H:%M:%S'))
                if min_time is None:
                    min_time = ts
                else:
                    if ts<min_time:
                        min_time = ts
                if max_time is None:
                    max_time = ts
                else:
                    if ts>max_time:
                        max_time = ts
            except ValueError:
                pass
    logging.info("Min-time:%s,Max-time:%s",min_time,max_time)
    return min_time,max_time

def main():
    MaxMinTime("ukr.txt")

if __name__=="__main__":
    main()

