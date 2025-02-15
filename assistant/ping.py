from Panda import start_time, pyrotgbot as bot
from pyrogram import filters

from Panda._func._helpers import get_readable_time
from Panda._func.assistant_helpers import _check_owner_or_sudos

@bot.on_message(filters.command(["ping"]) & filters.incoming)
@_check_owner_or_sudos
async def ping(client, message):
    uptime = get_readable_time((time.time() - start_time))
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await client.send_message(
        message.chat.id,
        f"**┏━《 **𝗣 𝗔 𝗡 𝗗 𝗔** 》━\n**┣➠  __Ping:__** `{ms}` \n ┗➠ __Uptime:__ `{uptime}`",
    )
