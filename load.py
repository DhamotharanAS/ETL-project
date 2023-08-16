import mysql.connector 
import pandas as pd
import json


#Load the configuration json file
f = open('config.json')

data = json.load(f)

f.close()

#Get the database information from the loaded data
mysql_db_config=data["target_database"]

#Establish the connection using the config
mydb = mysql.connector.connect(**mysql_db_config)

#Get the target denormalized tables names and file storing locations
denorm_tables_loc=data["Denormalized_tables"]
denorm_tables=list(denorm_tables_loc.keys())

for table in denorm_tables:
    
    dataframe = pd.read_csv(denorm_tables_loc[table])

    dataframe = dataframe[dataframe.columns[1:]]

    table_name = table
    
    cursor = mydb.cursor()

    # Insert values into the table
    insert_query = f'INSERT INTO {table_name} ({", ".join(dataframe.columns)}) VALUES ({", ".join(["%s"] * len(dataframe.columns))})'
    
    values = [tuple(row) for row in dataframe.values]
    
    cursor.executemany(insert_query, values)

# Commit the changes and close the connection
mydb.commit()
cursor.close()
mydb.close()

print('Table created and values inserted successfully.')
