import re
from collections import Counter
import csv


def reader(filename):
    with open(filename) as f:
        log = f.read()
      #  print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' #regex for ip search

        ips_list = re.findall(regexp, log)

        #print(ips_list)
        return ips_list

def count(ips_list):
    return Counter(ips_list)

def writecsv(counter):
    with open('output_ips.csv', 'w') as op:
        writer = csv.writer(op)

        header = ['IP', 'Count']

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]) )

if __name__ == '__main__':
    writecsv(count(reader('log.txt')))