import sqlite3


class Database:

    def __init__(self):
        self.database = sqlite3.connect("expenses.db")
        self.cursor = self.database.cursor()

    def create_table(self, table_name):
        CREATE_EXPENSES_SQL = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            month_year TEXT,
            reason TEXT,
            amount REAL
        );
        """
        self.cursor.execute(CREATE_EXPENSES_SQL)

db = Database()
#db.create_table("HAHAHA12")
