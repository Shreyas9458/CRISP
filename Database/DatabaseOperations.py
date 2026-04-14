import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

        return conn