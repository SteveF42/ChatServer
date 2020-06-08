import sqlite3
from datetime import datetime

FILE = 'messages.db'
TABLE = 'messages'

# c.execute("""CREATE TABLE messages (
#     first text,
#     time integer
# )""")

#c.execute("INSERT INTO messages VALUES ('you fucking racist','12:00')")

class database:
    def __init__(self):
        """
        creates the connection to file
        sets curser value
        creates new table if a table hasn't been created already
        """
        self.conn = sqlite3.connect(FILE)
        self.curser = self.conn.cursor()
        self._create_table()


    def _create_table(self):
        """
        creates a new table if there isn't already one active
        rtype: None
        """
        with self.conn:
            query = f'''CREATE TABLE IF NOT EXISTS {TABLE} (
                name text,
                message text,
                time Date,
                id INTEGER PRIMARY KEY AUTOINCREMENT 
            )'''
            self.curser.execute(query)


    def get_all_messages(self,limit=100,name=None):
        """
        type name: str
        rtype: returns a list of messages from a specific user
        """
        print (name)
        with self.conn:
            if not name:
                query = f'''SELECT * FROM {TABLE}'''
                self.curser.execute(query)
            else:
                query = '''SELECT * FROM %s WHERE name = :name''' % (TABLE)
                self.curser.execute(query,{'name':name})

        result = self.curser.fetchall()

        ls = []
        for r in sorted(result, key=lambda x: x[3], reverse=True)[:limit]:
            name, content, date, _id = r
            data = {"name":name, "message":content, "time":str(date)}
            ls.append(data)
            
        return list(reversed(ls))

    def insert_message(self,name, message):
        """
        inserts a new message for a selected user 
        type name: str
        type message: str
        rtype: none
        """
        with self.conn:
            query = f'''INSERT INTO {TABLE} VALUES (?,?,?,?)'''
            self.curser.execute(query,(name,message,datetime.now(),None))
            
    def close_connection(self):
        """
        closes connection to database
        rtype: None
        """
        self.conn.close()
