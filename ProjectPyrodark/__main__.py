# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/nathsupport & t.me/nathaellxx

import importlib

from pyrogram import idle
from uvloop import install

from config import *
from ProjectPyrodark import BOTLOG_CHATID, LOGGER, LOOP, bots
from ProjectPyrodark.helpers.misc import git, heroku

MSG_ON = """
🤖 **PYRONATH-USERBOT Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk mengecek Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("nathaellxx")
            await bot.join_chat("nathsupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("ProjectPyrodark").info("Starting PYRONATH-USERBOT")
    LOGGER("ProjectPyrodark").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("ProjectPyrodark").info(
        f"PYRONATH-USERBOT v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]"
    )
    LOOP.run_until_complete(main())
