from argparse import Action, ArgumentParser
import time

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        #namespace is --driver
        driver, destination= values #anything passed after --driver keyword
        namespace.driver = driver.lower() #s3 or local
        namespace.destination = destination #bucket_name or local_path


def create_parser():
    parser = ArgumentParser(description=""")
    Back up PostgreSQL database locally to aWS S3
    """)

    parser.add_argument("url", help="URL of the database to backup")
    # parser.add_argument('profile', help="Specify aws credentials profile which will be used in cli")
    parser.add_argument("--driver", '-d',
        help="how and where to store backup",
        nargs=2,
        metavar=('DRIVER', 'DESTINATION'),
        action=DriverAction,
        required=True)
    

    return parser

def main():
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    
    if args.driver == 's3':
        timestamp = time.strftime('%Y-%m-%dT%H-%M', time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        session = boto3.Session(profile_name='acg') #get passed from cli options
        client = session.client('s3')
        print(f"[I] Backing database up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing database up locally to {outfile.name}")
        storage.local(dump.stdout, outfile)

