import random
from pyrogram import Client, filters


STICKERS = ["CAACAgUAAxkBAAJzX2FUP7IYpFyxtbW8M4-jKp3ugvtSAAL6AgACE8GZVuZabx0YMtH3IQQ", "CAACAgUAAxkBAAJzZWFUP-V7gM_rw8MVFSoRdWDv4dkiAAJyAwACwRmYVsdTTuo8qbciIQQ"]


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	STICKER = random.choice(STICKERS)
	await msg.reply_sticker(STICKER)
