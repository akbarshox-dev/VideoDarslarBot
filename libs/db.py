import sqlite3


class DataBase:
    def __init__(self, db_name) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    
    def create_tables(self):
        try:
            with self.connection:
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id TEXT NOT NULL
                    role TEXT DEFAULT user 
                )''')
        
            print("Success")
        except:
            print("error")