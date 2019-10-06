import json
import sqlite3

conn = sqlite3.connect('manytomany.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2]
    #print(name, title, role)

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) ) #重複課程名稱的話，忽略他，然後在下一行中，
        #把原本就有輸入的可成名稱的id取出來，給予新人名一個對應的課程id
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    #cur.execute('''INSERT OR IGNORE INTO Member (role)
        #VALUES ( ? )''', ( role, ) ) #不能打這條，這樣role沒辦法跟user_id, course_id排在同一行

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role, ) ) #要這樣寫才會讓三個變數在同一行

    conn.commit()

strg = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X'''
#print(cur.execute(str))
for row in cur.execute(strg):
    print(str(row[0])) #要小心這邊要用str，前面的變數不能也設為str
#cur.execute(str)
cur.close()
