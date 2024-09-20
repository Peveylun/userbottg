from time import sleep
from random import seed, randint
from datetime import datetime

from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from bot.misc.parsers import parse_text


@Client.on_message(filters.command('type', prefixes='.') & filters.me)
async def type(_, msg: Message):
    orig_text = parse_text(msg)
    text = orig_text
    tbp = ''
    typing_symbol = '▉'
    while tbp != orig_text:
        try:
            await msg.edit(tbp + typing_symbol)
            sleep(0.05)
            tbp += text[0]
            text = text[1:]
            await msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            print(e)


@Client.on_message(filters.command('heart', prefixes='.') & filters.me)
async def heart(_, msg: Message):
    try:
        counter = 0
        hearts = ['❤❤❤', '🧡🧡🧡', '💛💛💛', '💚💚💚', '💙💙💙', '💜💜💜', '🖤🖤🖤', '🤍🤍🤍', '🤎🤎🤎']
        while counter != 5:
            for i in hearts:
                await msg.edit(i)
                sleep(1)
            counter += 1
    except FloodWait as e:
        print(e)


@Client.on_message(filters.command('хто', prefixes='.') & filters.me)
async def who(_, msg: Message):
    seed(datetime.now().timestamp())
    users_id = []
    async for i in Client.get_chat_members(_, msg.chat.id):
        users_id.append(i.user.id)
    orig_text = parse_text(msg)
    random_user = await Client.get_users(_, users_id[randint(0, len(users_id))])
    await msg.reply_text(f"{orig_text} {random_user.first_name} {random_user.last_name if random_user.last_name else ''}")
