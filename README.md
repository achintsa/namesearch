# namesearch
This is a database connect app made with python and flask which can be used to search names from database.
Please read instructions.txt for full installation and related details to run on your end.

I made this app on Ubuntu 14.04
python version 2.7.11 
flask version latest stable release as in August 2016 (0.11.x)

Database related Installations:

# Install MySQL server and related libraries
$ sudo apt-get install mysql-server
<set username password and remember>
$ sudo apt-get install libmysqlclient-dev

# Install MySQLdb
$ pip install flask-mysqldb


$ mysql -u root -p
 <password here>
 
# First create MySQL database

Run file named sampledb.py 
This would create the db of all permutation of firstnames.out and lastnames.out

<Important>
Now instructions to make python server endpoint to enable a user to search the database using firstname and lastname


# Firstly install virtualenv
Secondly install flask
http://flask.pocoo.org/docs/0.11/installation/
#for ubuntu
$ sudo apt-get install python-virtualenv

$ mkdir namesearch
$ cd namesearch
$ virtualenv venv
$ New python executable in venv/bin/python
Installing setuptools, pip............done.

$ . venv/bin/activate

#run app

$ python formdata.py
 * Running on http://127.0.0.1:5000/

open localhost or aforementioned link in browser (prefer google chrome)
http://127.0.0.1:5000/

Search for names!
