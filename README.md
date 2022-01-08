# First create virtualenv 

python3 -m virtualenv env_name

# activate virtualenv

cd env_name && bin/source/activate

# install project requirements

pip install -r requirements.txt


# install gdal-bin

sudo apt-get install gdal-bin


# Add postgis extension with postgres

1 ) sudo add-apt-repository ppa:ubuntugis/ppa
2 ) sudo apt-get update
3 ) sudo apt-get install postgis postgresql-10-postgis-2.5
4 ) sudo -u postgres psql


List all databases

5 ) \l

Connect to specific database

6 ) \c DATABASE_NAME

7 ) CREATE EXTENSION postgis;
8 ) CREATE EXTENSION postgis_topology;
9 ) \q
