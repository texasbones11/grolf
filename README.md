# grolf
#install Django on Ubuntu 18.04
apt-get install python-django

cd /var
django-admin startproject grolf
cd grolf

apt-get install mariadb-server
systemctl start mysql
mysql
create database grolfdb;
create user 'wjones'@`localhost` identified by 'XXXXXX';
grant all on grolfdb.* to 'wjones'@`localhost`;
apt-get install python-mysqldb python-pymysql
apt-get install build-essential python-dev libmysqlclient-dev

python manage.py migrate

python manage.py createsuperuser --username=wjones --email=XXXXXX
#create a password

# server is on port 8000
python manage.py runserver
