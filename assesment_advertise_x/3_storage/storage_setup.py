import boto3

s3 = boto3.client('s3')

def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)

# Example usage
create_bucket('advertisex-data-bucket')
