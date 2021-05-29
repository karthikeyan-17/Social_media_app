import sqlite3 as sql
def create_post (name, content):
    con =sql.connect('todo.db')
    cur=con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name,content))
    con.commit()
    con.close()

def get_posts():
    con=sql.connect('todo.db')
    cur=con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts





