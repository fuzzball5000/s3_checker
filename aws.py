import boto
from boto.s3.connection import Location

s3 = boto.connect_s3()
bucket = s3.lookup('osq')

try:
   read_bytes = open('currbytes', 'r')
except:
   print 'Failed to open file'
pass


total_bytes = 0
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

write_bytes = open('currbytes', 'w')
write_bytes.write(str(total_bytes))
