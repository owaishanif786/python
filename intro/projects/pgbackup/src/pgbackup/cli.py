from argparse import Action, ArgumentParser

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
    parser.add_argument("--driver", 
        help="how and where to store backup",
        nargs=2,
        action=DriverAction,
        required=True)

    return parser