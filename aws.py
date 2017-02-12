import boto
import sys
import pymongo
import datetime

from boto.s3.connection import Location
from pymongo import MongoClient
client = MongoClient()
db = client.AWSdb
s3 = boto.connect_s3()
bucket = s3.lookup(str(sys.argv[1]))
total_bytes = 0

try:
   read_bytes = open('currbytes', 'r+')
except:
   print 'Creating temp file'
   read_bytes = open('currbytes', 'w')
   read_bytes.write(str(total_bytes))
pass

for key in bucket:
    total_bytes += key.size
print total_bytes

for i in read_bytes:
    fluff = int(i)
    print fluff
    if total_bytes <= fluff:
        print "S3 storage isn't growing"
    elif total_bytes > fluff:
        print "S3 storage growing"
    else:
        print "Something else is going on, previous: %d current: %d" (total_bytes,i)

read_bytes.seek(0)
read_bytes.truncate()
read_bytes.write(str(total_bytes))
date=datetime.datetime.utcnow()
db.sizes.insert({"total" : total_bytes,"bucket" : sys.argv[1],'date': date})
print db.sizes.find_one()
for r in db.sizes.find({"bucket" : sys.argv[1]}):
    print r
read_bytes.close()
