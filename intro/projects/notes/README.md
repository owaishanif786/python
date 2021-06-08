webproject
==========

```shell
mkdir notes
cd notes
pipenv --python python3.7 install flask
mkdir templates static
touch {templates,static}/.gitkeep
curl   -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
touch __init__.py
    #create app there
flask run --host=0.0.0.0 --port=3000

#login to db server and create new database
sudo docker ps #check docker instance is running
sudo docker exec -i postgres psql postgres -U demo -c "CREATE DATABASE notes;"

# SQLAlchemy used as orm
create config.py and .env with db details and environment variables


```
