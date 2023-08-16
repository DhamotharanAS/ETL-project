import mysql.connector 
import json
import pandas as pd

#Load the configuration json file
f = open('config.json')

data = json.load(f)

f.close()

#Get the database information from the loaded data
mysql_db_config=data["database"]

#Establish the connection using the config
mydb = mysql.connector.connect(**mysql_db_config)

#Get the table names from the json data
tables=list(data["Normalized_tables"].keys())
table_loc=data["Normalized_tables"]

#for each table get the data into a dataframe and
#store it in the filename corresponding to the table
Query="SELECT * from "

for table in tables:

    df = pd.read_sql(Query+table,mydb)

    df.to_csv(table_loc[table])
    
print("Extraction Completed")
