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


```shell

#python setup.py bdist_wheel
#ls dist
#pip uninstall pgbackup-0.1.0-py3-none-any.whl
#pip install pgbackup-0.1.0-py3-none-any.whl
#pip install  https://pg-backups-001.s3.amazonaws.com/pgbackup-0.1.0-py3-none-any.whl
```

```python
>>> import boto3
>>> f = open('pgbackup-0.1.0-py3-none-any.whl', 'rb')
>>> session = boto3.Session(profile_name='acg')
>>> client = session.client('s3')
>>> client.upload_fileobj(f, 'pg-backups-001', 'pgbackup-0.1.0-py3-none-any.whl')
>>> exit()
```
