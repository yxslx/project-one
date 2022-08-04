import certifi
import os
import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
CLUSTER_NAME = os.environ["CLUSTER_NAME"]
DB_NAME = os.environ["DB_NAME"]
TABLE_NAME = os.environ["TABLE"]
URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER_NAME}.sfi8s.mongodb.net/?retryWrites=true&w=majority"
URL = os.environ["URL"]


def retrieve_data():
    df = pd.read_csv(URL, sep='\t', engine='python')
    return df


def conn():
    try:
        client = MongoClient(URI, tlsCAFile=certifi.where())
        db = client.test
        print("MongoDB cluster is reachable.")
        return client
    except ConnectionFailure as e:
        print("Could not connect to MongoDB")
        print(e)


def upload(client, df):
    try:
        db = client[f'{DB_NAME}']
        collection = db[F'{TABLE_NAME}']
        collection.insert_many(df.to_dict('records'))
        print('Upload complete')
    except Exception as e:
        print('Failed upload.')
        print(e)


def run_process():
    df = retrieve_data()
    client = conn()
    upload(client, df)


if __name__ == "__main__":
    run_process()
