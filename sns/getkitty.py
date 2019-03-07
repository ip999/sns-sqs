import boto3

# Create an SNS client
session = boto3.Session(profile_name='sqs', region_name='eu-west-1')
# Get the service resource
sns = session.client('sns')

# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:eu-west-1:896954218886:getkitty',
    Message='get me a kitty',
)

# Print out the response
print(response)