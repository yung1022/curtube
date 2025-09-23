import time
import random
print('CurTube v1.1')
def signin(Username, Password):
    issuccess = 0
    import sqlite3
    conn = sqlite3.connect('user_data.db') # Creates or connects to a database file
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        vidcount INTEGER NOT NULL,
        shortcount INTEGER NOT NULL,
        subs INTEGER NOT NULL,
        views INTEGER NOT NULL,
        lastupdatetime INTEGER NOT NULL
        )
    ''')
    conn.commit() # Save changes
    username = Username
    password_hash = Password # Store hashed passwords, not plain text!
    cursor.execute("SELECT * FROM users WHERE username = ?", (Username,))
    user_data = cursor.fetchone() # Fetch a single row
    if user_data:
        print(f"User already exists.")
        issuccess = 0
    else:
        cursor.execute("INSERT INTO users (username, password_hash, vidcount, shortcount, subs, views, lastupdatetime) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (username, password_hash, 0, 0, 0, 0, time.time()))
        conn.commit()
        issuccess = 1
    return issuccess
def data():
    import sqlite3
    conn = sqlite3.connect('user_data.db') # Creates or connects to a database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", ('idk',))
    user_data = cursor.fetchone() # Fetch a single row
    if user_data:
        print(f"User found: {user_data}")
def login(Username, Password):
    import sqlite3
    conn = sqlite3.connect('user_data.db') # Creates or connects to a database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (Username,))
    user_data = cursor.fetchone() # Fetch a single row
    if user_data:
        print(f"User found: {user_data[1]}")
        print('Logging in...')
        if user_data[2] == Password:
            global Useridlogedin
            Useridlogedin = user_data[0]
            print('Log in success, userid:', Useridlogedin)
            return Useridlogedin
        else:
            print('Log in failed, incorrect password')
            return 'error'
    else:
        print('User not found')
        return 'error'
def getalluser():
    import sqlite3
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users") # Replace 'your_table_name'
    user_data = cursor.fetchall()
    countid = 1
    for row in user_data:
        print('ID:', countid, ',', row) # Or perform other operations with each row
        countid += 1
def upload(type, title):
    import sqlite3
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vid (
        vidid INTEGER PRIMARY KEY AUTOINCREMENT,
        vidname TEXT NOT NULL,
        vidviews INTEGER NOT NULL,
        vidlikeratio INTEGER NOT NULL,
        vidwatchrate INTEGER NOT NULL,
        uploadtime INTEGER NOT NULL,
        laststatsupdatetime INTEGER NOT NULL,
        vidtype TEXT NOT NULL,
        viduploader TEXT NOT NULL
        )
    ''')
    print('Video Uploading...')
    cursor.execute("INSERT INTO vid (vidname, vidviews, vidlikeratio, vidwatchrate, uploadtime, laststatsupdatetime, vidtype, viduploader) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (title, 0, random.randrange(30, 100), random.randrange(40, 120), time.time(), time.time(), type, Useridlogedin))
    conn.commit()
    print('Upload Success')
    return 1