#Local
```
git clone git@github.com:krailastas/pubcloud.git 
$ virtualenv -p python3.6 pubcloud
$ . pubcloud/bin/activate
$ cd pubcloud
$ pip install -r requirements/dev.txt
$ python manage.py runserver
```

#Docker
```
$ sudo docker run -it -v pgdata:/var/lib/postgresql/data --name db -e POSTGRES_PASSWORD=YOUR_PASSWORD -d postgres:10.0-alpine
$ sudo docker exec db psql -U postgres -c "create role pubcloud with login superuser password 'YOUR_PASSWORD';"
$ sudo docker exec db psql -U postgres -c "create database pubcloud with owner=pubcloud;"
$ sudo docker run --name redis -v redisdata:/data -d redis:4-alpine redis-server --appendonly yes
$ sudo docker-compose pull
$ sudo docker-compose up -d
```
