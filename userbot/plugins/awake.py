"""
(((((((((((((((((((((((@LEGENDX22, @PythonProgramingIN)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22, @PythonProgramingIN)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22, @PythonProgramingIN)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22, @PythonProgramingIN)))))))))))))))))))))))))))
MADE BY @LEGENDX22, @PythonProgramingIN dont kang this plugin
CREDITS = @LEGENDX22 @PROBOYX @alain_champion, @PythonProgramingIN
Special thanks @alain_champion for this modified version
if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, legendversion, StartTime, CMD_HELP
from . import legend
from userbot.legend import BOT
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/fd0c6732fa1fdfeae2419.png"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   uptm = await Superior.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "💟 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 💟\n\n"
   ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 6.0.9\n\n"
   ALIVE_MESSAGE += "🔶 Superioir  𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔶 :   2.8\n\n"
   ALIVE_MESSAGE += f"🔷 𝚄𝙿𝚃𝙸𝙼𝙴 🔷 : {uptm}\n\n"
   ALIVE_MESSAGE += f"💠 𝙼𝚈 𝙱𝙾𝚂𝚂 💠: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += f"💠 [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-ROBOT) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/legendxop/legend-bot)  💠\n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
