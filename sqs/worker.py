import boto3
import time
import sys

session = boto3.Session(profile_name='sqs', region_name='eu-west-1')
# Get the service resource
sqs = session.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='myqueue.fifo')

# Process messages by printing out body
while 1:
    try:
        for message in queue.receive_messages():
            # Print out the body of the message
            print('Processed Message: {0}'.format(message.body))

            # Let the queue know that the message is processed
            message.delete()
    except:
        print("No messages in queue..")
        pass
    time.sleep(5)