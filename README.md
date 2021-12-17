# Sparkify Data Modeling #

Sparkify is a fictional music streaming service similar to spotify.
The goal of this project is to create an ETL pipeline transforming raw JSON data into a relational PostgreSQL database to be ready for analysis.<br/><br/>
The star schema can be described by this diagram:<br/><br/>
![image](https://user-images.githubusercontent.com/56934066/146473622-cf3e5564-bb71-45c0-8a47-02050449c064.png)

## Files ##
**data** - Contains the JSON files which includes both song data and log data.<br/>
**create_tables.py** - Is responsible for dropping any current tables and creates the sparkify database. This file uses the sql queries from sql_queries.py to perform these actions.<br/>
**sql_queries.py** - Holds all of the necessary sql queries to perform any action taken in the create_tables.py and etl.py files.<br/>
**etl.ipynb** - Pulls and pipelines a single record out of both song data and log data to confirm the insert scripts in sql_queries.py.<br/>
**etl.py** - Performs the pipeline of all song and log data into the sparkify database.<br/>
**test.ipynb** - Verifies the creation of the sparkify database as well as the inserts performed in etl.py and etl.ipynb.<br/>
## How To Run The ETL Pipeline ##
After downloading all necessary data and python files, make sure that all the dependencies are met.<br/>
First run:<br/>
*python create_tables.py*<br/>
Second run:<br/>
*python etl.py*
