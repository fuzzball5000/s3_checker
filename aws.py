import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
    total_size = 0
    for key in bucket.list():
        total_size += key.size
