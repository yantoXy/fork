# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB/blob/main/LICENSE/>.
#


import sys
import importlib
import heroku3
from pyrogram import idle
from uvloop import install
from Bdrl.config import BOTLOG_CHATID, BOT_TOKEN, HEROKU_APP_NAME, HEROKU_API_KEY

from Bdrl.version import __version__ as botver
from Bdrl import *
from Bdrl.helpers.misc import heroku, git
from Bdrl.logging import LOGGER


MSG_ON = """
✅ **Bdrl-Userbot Is Actived!**

➠ **Userbot Version -** `{}`
➠ **Try** `.alive` **for check your bot**
"""

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    y = Heroku.app(HEROKU_APP_NAME)
    heroku_var = y.config()
else:
    y = None


group_name = "My Bdrl Logs"
desc = "Log Groups Bdrl-Userbot.\n\nDon't leave from this group.\n\n✨ Powered By ~ @pantekyks


async def main():
    if bot:
        await bot.start()
        getbot = await bot.get_me()
        LOGGER("Assistant Bot").info(f"Started as {getbot.first_name} [{getbot.id}]")
    await app.start()
    get1 = await app.get_me()
    if not BOTLOG_CHATID:
        LOGGER("HEROKU").info("Creating your userbot logs...")
        try:
            _id = await app.create_supergroup(group_name, desc)
            gcid = int(str(f"{_id.id}"))
            await app.set_chat_photo(_id.id, photo="Bdrl/image/bdrl.jpg")
            heroku_var["BOTLOG_CHATID"] = gcid
        except Exception as e:
            LOGGER("HEROKU").error(str(e))
            LOGGER("HEROKU").warning(
                "see and set your var BOTLOG_CHATID. Create a telegram group then add @MissRose_Bot as co-founder and type /id, then put the id to var BOTLOG_CHATID"
            )
    else:
        pass
    try:
        await app.join_chat("gcaika")
        await app.join_chat("pantekyks")
        await app.send_message(
            BOTLOG_CHATID,
            MSG_ON.format(botver)
        )
    except:
        pass
    LOGGER("Client 1").info(f"Started as {get1.first_name} [{get1.id}]")
    if app2:
        await app2.start()
        get2 = await app2.get_me()
        try:
            await app2.join_chat("gcaika")
            await app2.join_chat("pantekyks")
            await app2.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            await app2.send_message(
                "me",
                MSG_ON.format(botver)
            )
            pass
        LOGGER("Client 2").info(f"Started as {get2.first_name} [{get2.id}]")
    if app3:
        await app3.start()
        get3 = await app3.get_me()
        try:
            await app3.join_chat("gcaika")
            await app3.join_chat("pantekyks")
            await app3.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            await app3.send_message(
                "me",
                MSG_ON.format(botver)
            )
            pass
        LOGGER("Client 3").info(f"Started as {get3.first_name} [{get3.id}]")
    if app4:
        await app4.start()
        get4 = await app4.get_me()
        try:
            await app4.join_chat("gcaika")
            await app4.join_chat("pantekyks")
            await app4.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            await app4.send_message(
                "me",
                MSG_ON.format(botver)
            )
            pass
        LOGGER("Client 4").info(f"Started as {get4.first_name} [{get4.id}]")
    if app5:
        await app5.start()
        get5 = await app5.get_me()
        try:
            await app5.join_chat("gcaika")
            await app5.join_chat("pantekyks")
            await app5.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            await app5.send_message(
                "me",
                MSG_ON.format(botver)
            )
            pass
        LOGGER("Client 5").info(f"Started as {get5.first_name} [{get5.id}]")
    LOGGER("Bdrl").info(f"Bot v{botver} is actived!")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
