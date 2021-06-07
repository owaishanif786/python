def local(inflie, outfile):
    outfile.write(inflie.read())
    outfile.close()
    inflie.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)

# PYTHONPATH=./src python
# import boto3
# >>> from pgbackup import storage
# >>> session = boto3.Session(profile_name='acg')
# >>> client = session.client('s3')
# >>> infile = open('example.txt', 'rb')
# >>> storage.s3(client, infile, 'pg-backups-001', infile.name)