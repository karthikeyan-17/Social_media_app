import sqlite3

con = sqlite3.connect('todo.db')

sql_query = """
CREATE TABLE posts (
      id INTEGER PRIMARY KEY,
      name TEXT not null,
      content text not null
);
"""

con.execute(sql_query)
con.close()