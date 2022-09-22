from time import sleep

from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message


@Client.on_message(filters.command('type', prefixes='.') & filters.me)
async def type(_, msg: Message):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
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
