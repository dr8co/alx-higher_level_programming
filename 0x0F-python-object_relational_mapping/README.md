# 0x0F. Python - Object-relational mapping

This project aims to link databases and Python.

In the first part, the module MySQLdb was used to connect to a MySQL database and execute SQL queries.

In the second part, the module SQLAlchemy, an Object Relational Mapper (ORM), was used to achieve the same.

## General Learning Objectives

* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What `ORM` means
* How to map a Python Class to a MySQL table

## Requirements

### Ubuntu 20.04 LTS

[install Ubuntu 20.04]()

### Python 3.8.5

[Install Python]()

### MySQL 8.0

[Install MySQL 8]()

### `MySQLdb 2.0.x`

#### Install `MySQLdb` module version `2.0.x`

```console
user@host:~$ sudo apt-get install python3-dev
user@host:~$ sudo apt-get install libmysqlclient-dev
user@host:~$ sudo apt-get install zlib1g-dev
user@host:~$ sudo pip3 install mysqlclient
...
user@host:~$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### `SQLAlchemy 1.4.x`

#### Install `SQLAlchemy` module version `1.4.x`

```console
user@host:~$ sudo pip3 install SQLAlchemy
...
user@host:~$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

