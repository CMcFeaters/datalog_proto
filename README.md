# datalog_proto
Prototype of large database parser widget.  Thsi is going to be the thing between the massive DB and the R program that converts the DB into usable chunks

----packages----
Uses mariaDB as the database server and client
-mariadb: https://mariadb-corporation.github.io/mariadb-connector-python/

Uses Python3
Uses sqlalchemy
-https://www.sqlalchemy.org/

uses python-dotenv 0.15.0
"pip install python-dotenv"
https://pypi.org/project/python-dotenv/

1) The *.env file contians your access info to the database.  should be located in [program direcroty]
2) The *.env should contain 2 variables
uname="whatever_the_key_is"
pw="whatever_the_secret_is" 

----files----
'test_python_interface_alch'
-this is the test schema for this database.  Runnign this as main will create a roughly 80M row DB of about 20GB.  See "datalog_schema" for schema

'timing'
-timer tool for testing

'basic_loader'
-this is the start of the data log loader, this will be the thing that pulls this massive DB into a bunch of little DBs

'datalog_schema.sql'
-schema for the datalog