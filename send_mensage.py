import boto3

# Create SQS client
sqs = boto3.client('sqs',region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/099580720453/renan'


def send_message():
# Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=0,
        MessageBody=(
            'Oie galerinha'
        )
    )

for _ in range(200):
    send_message()
    
