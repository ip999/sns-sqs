import boto3

#set session
session = boto3.Session(profile_name='sqs', region_name='eu-west-1')
sqs = session.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='myqueue.fifo')

userInput = ""

while 1:
    try:
        userInput = input("Enter a message: ")
        response = queue.send_message(
            MessageBody=userInput,
            MessageGroupId='messageGroup1'
        )
        # The response is NOT a resource, but gives you a message ID and MD5
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))

    except NameError:
        pass