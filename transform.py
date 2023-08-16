import json 
import pandas as pd
import re

 

#Load the configuration json file
f = open('config.json')

 

data = json.load(f)

 

f.close()

 

#Get the normalized tables and their locations from json data
norm_tables_loc=data["Normalized_tables"]
norm_tables=list(norm_tables_loc.keys())

 

#Get the target denormalized tables names and file storing locations
denorm_tables_loc=data["Denormalized_tables"]
denorm_tables=list(denorm_tables_loc.keys())

 

#get the transformation details from the json data
transformations=data["transformations"]

 

#Now for each transformation make the appropriate operation.

 

def concat_op(df,src_column,target_column):

    df[target_column] = df[src_column[0]].map(str) +' ' + df[src_column[1]].map(str)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    return df

 

def change_date_format_op(df,src_column,target_column):

    temp=[]
    for i in df[src_column]:
        x=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', i)
        temp.append(x)
    df[target_column]=temp
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    return df

 

def split_op(df,src_column, target_columns):

 

    df[target_columns] = df[src_column[0]].str.split(',', expand=True)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

 

    return df

 

def drop_op(df, src_columns):

    df=df.drop(src_columns,axis=1)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

 

    return df

 

def join_op(df1, df2, join_criteria, join_type):

 

    df3=df1.merge(df2, how= join_type,
                      left_on=join_criteria["table1"],\
                      right_on=join_criteria["table2"])
    df3 = df3.loc[:, ~df3.columns.str.contains('^Unnamed')]

 

    return df3

for transform in transformations:
    if transform["operation"] == "concat":

        df = pd.read_csv(norm_tables_loc[transform["src_table"]])

        df = concat_op(df,transform["src_column"],transform["target_column"])

        df.to_csv(norm_tables_loc[transform["src_table"]])

 

    elif transform["operation"] == "change_date_format":

 

        df = pd.read_csv(norm_tables_loc[transform["src_table"]])

 

        df = change_date_format_op(df, transform["src_column"], transform["target_column"])

 

        df.to_csv(norm_tables_loc[transform["src_table"]])

    elif transform["operation"] == "split":

        df = pd.read_csv(norm_tables_loc[transform["src_table"]])

 

        df = split_op(df, transform["src_column"],transform["target_columns"])

        df.to_csv(norm_tables_loc[transform["src_table"]])

    elif transform["operation"] == "drop":

        df = pd.read_csv(norm_tables_loc[transform["src_table"]])

        df=drop_op(df, transform["src_columns"])

        df.to_csv(norm_tables_loc[transform["src_table"]])

    elif transform["operation"] == "join":

 

        df1 = pd.read_csv(norm_tables_loc[transform["src_tables"]["table1"]])

 

        df2 = pd.read_csv(norm_tables_loc[transform["src_tables"]["table2"]])

 

        df3 = join_op(df1, df2, transform["join_criteria"], transform["join_type"])

        df3.to_csv(denorm_tables_loc[transform["target_name"]])

    else:
        pass
