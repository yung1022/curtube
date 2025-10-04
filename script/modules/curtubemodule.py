API_BASE = "https://didactic-space-sniffle-w4jp57gvgvv2vgw5-5000.preview.app.github.dev"
# 讓 Python 可以顯示訊息到 <div id="text"></div>
from pyscript import document

def show_message(msg):
    text_div = document.getElementById("text")
    text_div.innerText = msg
import time
import random
import asyncio
import json

from js import document
import js
import asyncio
import json

    # ''')
    # conn.commit() # Save changes
    # username = Username

# 註冊帳號，呼叫 Flask API
def signin(event):
    Username = document.querySelector("#loginusername").value
    Password = document.querySelector("#loginpassword").value
    async def register():
        headers = js.eval('({"Content-Type": "application/json"})')
        resp = await js.fetch(
            f"{API_BASE}/api/register",
            method="POST",
            headers=headers,
            body=json.dumps({"username": Username, "password": Password})
        )
        if resp.status == 200:
            show_message("Account created!")
        else:
            data = await resp.json()
            show_message("Register failed: " + str(data.get("error")))
    asyncio.ensure_future(register())
    # password_hash = Password # Store hashed passwords, not plain text!
'''def data():
    import sqlite3
    conn = sqlite3.connect('user_data.db') # Creates or connects to a database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", ('idk',))
    user_data = cursor.fetchone() # Fetch a single row
    if user_data:
        print(f"User found: {user_data}")'''
def login(event):
    Username = document.querySelector("#loginusername").value
    Password = document.querySelector("#loginpassword").value
    async def do_login():
        headers = js.eval('({"Content-Type": "application/json"})')
        resp = await js.fetch(
            f"{API_BASE}/api/login",
            method="POST",
            headers=headers,
            body=json.dumps({"username": Username, "password": Password})
        )
        if resp.status == 200:
            show_message("Login success!")
        else:
            data = await resp.json()
            show_message("Login failed: " + str(data.get("error")))
    asyncio.ensure_future(do_login())
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
def upload(event):
    from pyscript import document
    import random
    import time
    Useridlogedin = 1 # this is a test
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
    input_text = document.querySelector("#vidtitle")
    cursor.execute("INSERT INTO vid (vidname, vidviews, vidlikeratio, vidwatchrate, uploadtime, laststatsupdatetime, vidtype, viduploader) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (input_text, 0, random.randrange(30, 100), random.randrange(40, 120), time.time(), time.time(), "video", Useridlogedin))
    conn.commit()
    print('Upload Success')
    return 
def getallvid(event):
    from pyscript import document
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
    cursor.execute("SELECT * FROM vid")
    vid_data = cursor.fetchall()
    print(vid_data)
    output_div = document.querySelector("#vidout")
    output_div.innerText = vid_data

