import pandas as pd
import numpy as np

def drop_columns(df,list_of_columns):
    for column in list_of_columns:
        df = df.drop(f"{column}",axis=1)
        print(f"Succesfully dropped {column}")
    return df

def replace_na(df,list_of_columns,data_type="str"):
    for column in list_of_columns:
        if data_type == "str":
            df[f'{column}'] = df[f'{column}'].replace('NA', '')
        else:
            df[f'{column}'] = df[f'{column}'].astype('str')  # Convert to string to handle errors
            df[f'{column}'] = df[f'{column}'].replace('NA', pd.NA)
            if data_type == 'int':
                df[f'{column}'] = df[f'{column}'].astype('int') # Convert back to integer
            elif data_type == 'float':
                df[f'{column}'] = df[f'{column}'].astype('float') # Convert back to float
            elif data_type == 'bool':
                df[f'{column}'] = df[f'{column}'].astype('bool') # Convert back to boolean
            elif data_type == "str":
                pass
            else:
                print(f'{column} is not an integer, float, boolean or string value!')
    return df

def remove_rows(df,column,value):
    df = df[df[f'{column}'] != f'{value}']
    return df

def merge_frames(df1,df2,columns1,columns2):
    merged_df = pd.merge(df1, df2, left_on=columns1,
                     right_on=columns2)
    return merged_df

def divide_columns(df,list_of_columns):
    for column in list_of_columns:
        df[f'{column}'] = df[f'{column}'].astype('float')
        df[f'{column}'] = df[f'{column}']/100
        print(f'column: {column} has been divided by 100')
    return df