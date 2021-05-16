import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, level TEXT, "
                    "name TEXT, chord TEXT, score INTEGER)")
        self.conn.commit()

    def insert(self,level, name, chord, score):
        #the NULL parameter - auto-incremented id
        self.cur.execute("INSERT INTO scores VALUES(NULL,?,?,?,?)", (level,name,chord,score))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM scores")
        rows = self.cur.fetchall()

        return rows

    def search(self,level="", name="", chord="", score=""):
        self.cur.execute("SELECT * FROM scores WHERE level = ? OR name = ? OR chord = ? "
                    "OR score = ?", (level, name, chord, score))
        rows = self.cur.fetchall()
        
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM scores WHERE id = ?", (id,))
        self.conn.commit()
        

    def update(self,id, level, name, chord, score):
        self.cur.execute("UPDATE scores SET level = ?, name = ?, chord = ?, score = ? WHERE id = ?", (level, name, chord, score, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
