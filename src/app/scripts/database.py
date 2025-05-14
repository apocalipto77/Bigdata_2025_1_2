import sqlite3
import pandas as pd

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table_from_df(self, df, table_name):
        cols = df.columns
        cols_with_types = ', '.join([f'"{col}" TEXT' for col in cols])
        self.cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        self.cursor.execute(f'CREATE TABLE {table_name} ({cols_with_types})')
        self.conn.commit()

    def insert_dataframe(self, df, table_name):
        placeholders = ', '.join(['?'] * len(df.columns))
        for _, row in df.iterrows():
            self.cursor.execute(
                f'INSERT INTO {table_name} VALUES ({placeholders})',
                tuple(str(x) for x in row)
            )
        self.conn.commit()

    def query_all(self, table_name, limit=5):
        self.cursor.execute(f'SELECT * FROM {table_name} LIMIT {limit}')
        return self.cursor.fetchall()
