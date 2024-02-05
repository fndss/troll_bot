import json
import random
from pyrogram import Client, filters
from pyrogram.client import Client

api_id = "1"
api_hash = "b6b154c3707471f5339bd661645ed3d6"
bot_token = ""

# open "data_base" file
with open("result.json", "r", encoding="utf-8") as f:
    buff = json.load(f)

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# add user id in triggers_id list
@app.on_message(filters.user(buff["bogi_imperatori"]) & filters.command("setdaun"))
async def add_daun(client, message):
    global buff
    if not message.reply_to_message:
        await message.reply_text("комманда должна отвечать на сообщение")
        return
    if message.reply_to_message.from_user.id in buff["bogi_imperatori"]:
        await message.reply_text("это бог император", quote=True)
        return
    try:
        buff['dauns'].append(message.reply_to_message.sender_chat.id)
        with open("result.json", "w", encoding="utf-8") as f1:
            json.dump(buff, f1, indent=4, ensure_ascii=False)
        await message.reply_text("🫵, @" + (str)(message.reply_to_message.sender_chat.username) + " ТЫ ДАУН!", quote=True)
    except:
        buff['dauns'].append(message.reply_to_message.from_user.id)
        with open("result.json", "w", encoding="utf-8") as f1:
            json.dump(buff, f1, indent=4, ensure_ascii=False)
        await message.reply_text("🫵, @" + (str)(message.reply_to_message.from_user.username) + " ТЫ ДАУН!", quote=True)

# delete user id out on triggers_id list
@app.on_message(filters.user(buff["bogi_imperatori"]) & filters.command("deldaun"))
async def del_daun(client, message):
    global buff
    if not message.reply_to_message:
        await message.reply_text("комманда должна отвечать на сообщение")
        return
    try:
        buff['dauns'].remove(message.reply_to_message.sender_chat.id)
        with open("result.json", "w", encoding="utf-8") as f1:
            json.dump(buff, f1, indent=4, ensure_ascii=False)
        await message.reply_text("🫵, @" + (str)(message.reply_to_message.sender_chat.username) + " ТЫ ВЫПИСАН ИЗ ДАУНОВ!", quote=True)
    except:
        buff['dauns'].remove(message.reply_to_message.from_user.id)
        with open("result.json", "w", encoding="utf-8") as f1:
            json.dump(buff, f1, indent=4, ensure_ascii=False)
        await message.reply_text("🫵, @" + (str)(message.reply_to_message.from_user.username) + " ТЫ ВЫПИСАН ИЗ ДАУНОВ!", quote=True)


#reply random message out on text_troll list
@app.on_message(filters.incoming)
async def reply_to_user(client, message):
    try:
        if message.sender_chat.id in buff["dauns"]:
            await message.reply_text(buff["responses"][random.randrange(len(buff["responses"]))], quote=True)
    except:
        if message.from_user.id in buff["dauns"]:
            await message.reply_text(buff["responses"][random.randrange(len(buff["responses"]))], quote=True)

app.run()