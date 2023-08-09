#!usr/bin/env python3

# build a functions that returns all of the buckets in my s3 account

import boto3


def get_buckets():
    s3 = boto3.resource("s3")
    for bucket in s3.buckets.all():
        print(bucket.name)
        

if __name__ == "__main__":
    get_buckets()
