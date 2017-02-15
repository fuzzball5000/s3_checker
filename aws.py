import boto
import sys
import pymongo
import datetime

from boto.s3.connection import Location
from pymongo import MongoClient
client = MongoClient()
db = client.AWSdb
s3 = boto.connect_s3()

for i in sys.argv[1:]:
    print i
    total_bytes = 0
    bucket = s3.lookup(str(i))
    print bucket
    for key in bucket:
        total_bytes += key.size
    print total_bytes

    date=datetime.datetime.utcnow()
    db.sizes.insert({"total" : total_bytes,"bucket" : i,'date': date})

for r in db.sizes.find():
    print r
