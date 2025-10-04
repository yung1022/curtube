import js
import asyncio
import json

# 註冊新帳號
async def register(username, password):
    resp = await js.fetch(
        "/api/register",
        method="POST",
        headers={"Content-Type": "application/json"},
        body=json.dumps({"username": username, "password": password})
    )
    if resp.status == 200:
        print("註冊成功！")
    else:
        data = await resp.json()
        print("註冊失敗：", data.get("error"))

# 登入
async def login(username, password):
    resp = await js.fetch(
        "/api/login",
        method="POST",
        headers={"Content-Type": "application/json"},
        body=json.dumps({"username": username, "password": password})
    )
    if resp.status == 200:
        print("登入成功！")
    else:
        data = await resp.json()
        print("登入失敗：", data.get("error"))

# 取得所有帳號（不含密碼雜湊）
async def get_users():
    resp = await js.fetch("/api/userdata")
    data = await resp.json()
    print("所有帳號：", data)

# 使用方式（PyScript 內呼叫）
# import asyncio
# asyncio.ensure_future(register("testuser", "testpass"))
# asyncio.ensure_future(login("testuser", "testpass"))
# asyncio.ensure_future(get_users())
