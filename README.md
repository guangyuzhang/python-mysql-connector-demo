## Python MySQL Connector Demo



### Introduction

This repository is for python mysql connector training.

### Prerequisites

mysql.connector


### Installation

Download and install MySQL Connector:
```
$ cd ~/tools
$ wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.22.tar.gz
$ tar xzf mysql-connector-python-8.0.22.tar.gz
$ cd ~/tools/mysql-connector-python-8.0.22
$ sudo python3 setup.py install
```

Sign up an account at freemysqlhosting.net

Download the sql script file from:
```
$ wget https://github.com/myems/myems-database/blob/master/myems_system_db.sql
```

Replace 'myems_system_db' with your own database name in the script.

Run the sql script in phpMyAdmin at db4free.net

Modify the config.py with your own account at db4free.

### References

[1]. https://www.freemysqlhosting.net/

[2]. https://dev.mysql.com/doc/connector-python/en/

[3]. https://dev.mysql.com/downloads/connector/python/
