from pyrogram import Client, filters
from pyrogram.types import Message

from bot.misc.todo_db import DB
from bot.misc.useful_functions import parse_text

db = DB('database.db')


@Client.on_message(filters.command('add', prefixes='.') & filters.me)
async def add(_, msg: Message):
    temp = parse_text(msg)
    db.create(temp)
    await msg.edit(f'Added to DB: {temp}')


@Client.on_message(filters.command('get', prefixes='.') & filters.me)
async def get(_, msg: Message):
    try:
        await msg.edit(db.get())
    except:
        await msg.edit("Empty.")


@Client.on_message(filters.command('delete', prefixes='.') & filters.me)
async def delete(_, msg: Message):
    db.delete(parse_text(msg))
