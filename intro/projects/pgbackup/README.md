pgbackup cli tool
=================

s3 Example w/ bucket name:

```shell
gbackup postgres://username@ip:port/db_name --driver s3 bucket_name
```

Local Example w/ local path:

```shell
pgbackup postgres://username@ip:port/db_name --driver local /path/to/file
```

## Installation From Source

To install the package after you've cloned the repositor, you'll want to run the following comand from within the project directory:

```shell
pip install --user -e
```

## Preparing for Development

Follow these steps to start developing with this project

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/pgbackup`
3. `cd` into repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
