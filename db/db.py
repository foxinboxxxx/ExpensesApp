import sqlite3

CREATE_EXPENSES_SQL = """
CREATE TABLE IF NOT EXISTS expenses (
    month_year TEXT,
    reason TEXT,
    amount REAL
);
"""

database = sqlite3.connect("expenses.db")
cursor = database.cursor()
cursor.execute(CREATE_EXPENSES_SQL)
pass