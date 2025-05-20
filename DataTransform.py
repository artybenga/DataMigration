import pandas as pd
import psycopg2
import glob
from os import listdir
from sqlalchemy import create_engine


def csv_to_db():
    # create connection and connect to DB
    conn = psycopg2.connect(f"host=localhost dbname=ClioInterview user=postgres password=wogman")
    cur = conn.cursor()
    engine = create_engine('postgresql+psycopg2://postgres:wogman@localhost/ClioInterview')
    # Read the CSV file into a DataFrame
    for filename in read_csv_filenames():
        df = pd.read_csv(filename)
        # Perform the data loading operation
        df.to_sql(filename.replace(".csv", ''), con=engine, if_exists='replace', index=False)
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()

def data_transform():
    contacts = pd.read_csv("contacts.csv")
    matters = pd.read_csv("matters.csv")
    # new_df_1 = df[['col_A', 'col_C']]
    result = pd.concat([matters, contacts], axis=1, join="outer")
    print(result)


def read_csv_filenames():
    txtfiles = []
    for file in glob.glob("*.csv"):
        txtfiles.append(file)
    return txtfiles


#data_transform()
csv_to_db()
# read_csv_filenames()