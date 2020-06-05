import sqlite3

FILE = 'messages.db'
TABLE = 'messages'

# c.execute("""CREATE TABLE messages (
#     first text,
#     time integer
# )""")

#c.execute("INSERT INTO messages VALUES ('you fucking racist','12:00')")

class database:
    def __init__(self):
        self.conn = sqlite3.connect(FILE)
        self.curser = self.conn.cursor()
        self._create_table()



    def _create_table(self):
        
        with self.conn:
            query = f'''CREATE TABLE IF NOT EXISTS {TABLE} (
                name text,
                message text
            )'''
            self.curser.execute(query)

    def get_message(self,name=None,limit=100):
        print (name)
        with self.conn:
            if not name:
                query = f'''SELECT * FROM {TABLE}'''
                self.curser.execute(query)
            else:
                query = '''SELECT * FROM %s WHERE name = :name''' % (TABLE)
                self.curser.execute(query,{'name':name})

        result = self.curser.fetchall()
        return result


    def insert_message(self,name, message):

        with self.conn:
            query = f'''INSERT INTO {TABLE} VALUES (?,?)'''
            self.curser.execute(query,(name,message))
    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    c = database()
    s = c.get_message()
    for i in s:
        print(i)