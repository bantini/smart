__author__ = 'nilayan'
import csv
import os
from os.path import join
path = "C:/Users/nilayan/Google Drive/Data/ukr_expt2.csv"
with open(path,'r') as reader:
    csv_reader = csv.reader(reader)
    sum1 = 0
    counter1 = 0
    sum2 = 0
    counter2 = 0
    sum3 = 0
    counter3 = 0
    sum4 = 0
    counter4 = 0
    for row in csv_reader:
        if int(row[1]) == 1 and int(row[0]) == 1:
            sum1+=float(row[5])
            counter1+=1
        if int(row[2])== 1 and int(row[0]) == 1:
            sum2+=float(row[5])
            counter2+=1
        if int(row[3])== 1 and int(row[0]) == 1:
            sum3+=float(row[5])
            counter3+=1
        if int(row[4])== 1 and int(row[0]) == 1:
            sum4+=float(row[5])
            counter4+=1
    try:
        quotient1 = float(sum1)/counter1
    except ZeroDivisionError:
        quotient1 = 0
    try:
        quotient2 = float(sum2)/counter2
    except ZeroDivisionError:
        quotient2 = 0
    try:
        quotient3 = float(sum3)/counter3
    except ZeroDivisionError:
        quotient3 = 0
    try:
        quotient4 = float(sum4)/counter4
    except ZeroDivisionError:
        quotient4 = 0

    print('%d,%f,%d,%f,%d,%f,%d,%f'%(counter1,quotient1,counter2,quotient2,counter3,quotient3,counter4,quotient4))


