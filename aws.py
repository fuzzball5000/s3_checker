import boto
from boto.s3.connection import Location

s3 = boto.connect_s3()
bucket = s3.lookup('osq')
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
        print "Something else is going on ",'%d %d' (total_bytes,i)

read_bytes.seek(0)
read_bytes.truncate()
read_bytes.write(str(total_bytes))
read_bytes.close()
