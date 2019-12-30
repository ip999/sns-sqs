import boto3
import uuid 

#set session
session = boto3.Session(profile_name='sqs', region_name='eu-west-1')
sqs = session.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='myqueue.fifo')

userInput = ""

count = 0

while (count < 20):
    try:
        #userInput = input("Enter a message: ")
        messageID = str(uuid.uuid1()).join(str(count))
        response = queue.send_message(
            MessageBody=messageID,
            MessageGroupId='messageGroup1'
        )
        # The response is NOT a resource, but gives you a message ID and MD5
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
        count = count + 1

    except NameError:
        pass

print(count, " Messages Created")