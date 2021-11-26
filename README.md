# datalog_proto
A simple proof of concept to resolve the issue of dealing with a DB that is larger than available memory in R.  This program functions as a widget between the DB and the R program, running a simple DB query on the DB and producing a *.csv of the results.  

The files contained here include a means to develop the large DB, the DB schema, and a simple loader that creates the .csv.

----SETUP----

for a list of packages see "packages.txt"

Uses mariaDB as the database server and client
-mariadb: https://mariadb-corporation.github.io/mariadb-connector-python/

Uses a *.env setup for database access.  The following shoudl be setup:
https://pypi.org/project/python-dotenv/

1) The *.env file contians your access info to the database.  should be located in [program direcroty]
2) The *.env should contain 2 variables
uname="whatever_the_key_is"
pw="whatever_the_secret_is" 

----files----

'test_python_interface_alch'

-this is the test schema for this database.  Runnign this as main will create a roughly 80M row DB of about 20GB.  See "datalog_schema" for schema

'basic_loader'

-this is the start of the data log loader, this will be the thing that queries the DB and produces a manageable csv file

'data_generator'

-juat builds a roughly 18gb database.  Warning, not optimized and takes a long time

'datalog_schema.sql'

-schema for the datalog, produced using mariadb sql with:
"mysqldump -h yourhostnameorIP -u root -p --no-data dbname > datalog_schema.sql"
