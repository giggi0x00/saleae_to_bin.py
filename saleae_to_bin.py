import csv
import sys
import codecs


f=open("/tmp/dump.bin","ba")


csvfile=open(sys.argv[1],'r');
spamreader = csv.reader(csvfile, delimiter=',')
s=""
print("loadded ",sys.argv[1])
next(spamreader,None);
for row in spamreader:
   val=row[2].strip();
   data=int(val, 16).to_bytes(1,"little")
   f.write(data)
f.close()


print("Execute strings /tmp/dump.bin")
