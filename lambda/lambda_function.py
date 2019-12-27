import boto3
import urllib
import json
import urlparse, os
import uuid
from botocore.vendored import requests
#import requests

BUCKET_NAME = 'randomkitties'
TMP_FILE = "/tmp/kitty.jpg"
KITTY_API = "https://aws.random.cat/meow"

def lambda_handler(event, context):
    kittyfile = urllib.URLopener()
    try:
        
        r = requests.get(KITTY_API)
        data = r.json()
        print(r.json())
        print(data['file'])
        KITTY_URL = data['file']

        kittyfile.retrieve(KITTY_URL, TMP_FILE)

        print("got kitty")

        s3 = boto3.client('s3')
        
        a = urlparse.urlparse(KITTY_URL)
        b = os.path.basename(a.path)
        print(b)
        
        filename, file_extension = os.path.splitext(b)
        print(file_extension)
        
        unique_filename = str(uuid.uuid4()) + file_extension
        print(unique_filename)
        
        with open(TMP_FILE) as file:
            object = file.read()
            s3.put_object(Body=object, Bucket=BUCKET_NAME, Key=unique_filename)

    except Exception as e:
        print(e)
        raise e
