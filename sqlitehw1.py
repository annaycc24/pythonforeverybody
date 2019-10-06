import sqlite3
conn = sqlite3.connect("sqlitehw1.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Ages")
cur.execute("CREATE TABLE Ages (name VARCHAR(128),age INTEGER)")
cur.execute("DELETE FROM Ages")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Jebadiah', 17)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Taddy', 25)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Nureza', 29)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Latif', 25)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Islay', 20)")
#hex()會把字串轉成16進位，SELECT...AS...是把hex(name || age)暫存為Ｘ
#name || age是concatenate the name column to the age column
result = "SELECT hex(name || age) AS X FROM Ages ORDER BY X" #Integers whose character values (according to the ASCII table) are to be retrieved.
for row in cur.execute(result):
    print(str(row[0]))
cur.close()
